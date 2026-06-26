from typing import List
import math

from models.state_vector import StudentState
from models.agent_prediction import ContributingFactor


class TaskDecision:
    """
    Output object for each task decision.
    """

    def __init__(self, task, priority_score, action, reason, factors):
        self.task = task
        self.priority_score = priority_score
        self.action = action
        self.reason = reason
        self.factors = factors


class DecisionEngine:
    """
    Core reasoning engine of ARWA.
    Converts StudentState → ranked recovery actions.
    """

    def __init__(self):

        self.weights = {
            "grade_impact": 1.5,
            "urgency": 2.0,
            "difficulty_penalty": 1.0,
            "burnout_penalty": 2.5,
        }

    # -------------------------
    # FEATURE ENGINEERING
    # -------------------------
    def compute_task_features(self, task, state: StudentState):

        urgency = math.exp(-task["due_in_hours"] / 24)

        grade_impact = task["points_value"] * self.weights["grade_impact"]

        difficulty_penalty = task["difficulty"] / 10

        burnout_factor = state.burnout_risk.score * task["estimated_time"]

        return {
            "urgency": urgency,
            "grade_impact": grade_impact,
            "difficulty_penalty": difficulty_penalty,
            "burnout_factor": burnout_factor,
        }

    # -------------------------
    # SCORING CORE
    # -------------------------
    def score_task(self, task, state: StudentState):

        f = self.compute_task_features(task, state)

        score = (
            f["grade_impact"] * f["urgency"] * self.weights["urgency"]
        ) / (
            task["estimated_time"]
            + f["difficulty_penalty"]
            + f["burnout_factor"] * self.weights["burnout_penalty"]
        )

        # --- burnout override ---
        if state.burnout_risk.score > 0.7 and task["difficulty"] > 7:
            score *= 0.5

        # --- urgency override ---
        if task["due_in_hours"] < 6:
            score *= 2.0

        return score, f

    # -------------------------
    # ACTION POLICY
    # -------------------------
    def decide_action(self, task, score, state: StudentState):

        if task["points_value"] < 5 and task["due_in_hours"] > 48:
            return "DROP", "Low impact and not urgent"

        if state.burnout_risk.score > 0.8 and task["difficulty"] > 7:
            return "DELAY", "High burnout risk detected"

        if task["due_in_hours"] < 8:
            return "DO", "Deadline critical"

        if score > 8:
            return "DO", "High priority recovery task"

        return "DELAY", "Lower priority than alternatives"

    # -------------------------
    # MAIN REASONING LOOP
    # -------------------------
    def optimize(self, state: StudentState):

        decisions = []

        for task in state.tasks:

            score, factors = self.score_task(task, state)

            action, reason = self.decide_action(task, score, state)

            # convert raw factors → explainability format
            explanation_factors = [
                ContributingFactor(
                    factor="urgency",
                    contribution=round(factors["urgency"] * 100, 1),
                    explanation="How close the deadline is"
                ),
                ContributingFactor(
                    factor="grade_impact",
                    contribution=round(factors["grade_impact"], 1),
                    explanation="Impact on overall grade"
                ),
                ContributingFactor(
                    factor="burnout_pressure",
                    contribution=round(factors["burnout_factor"], 1),
                    explanation="Estimated fatigue cost"
                ),
            ]

            decisions.append(
                TaskDecision(
                    task=task,
                    priority_score=score,
                    action=action,
                    reason=reason,
                    factors=explanation_factors
                )
            )

        # SORT = CORE AI BEHAVIOR
        decisions.sort(key=lambda x: x.priority_score, reverse=True)

        return decisions