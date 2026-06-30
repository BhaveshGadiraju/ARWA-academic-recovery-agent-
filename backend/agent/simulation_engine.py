from agent.candidate_plan_generator import CandidatePlanGenerator
from agent.recovery_evaluator import RecoveryEvaluator
from agent.beam_search import BeamSearchPlanner


class SimulationEngine:
    """
    Simulates multiple academic recovery strategies.

    Pipeline:
        Student Tasks
              ↓
        Beam Search Planner
              ↓
        Candidate Recovery Plans
              ↓
        Recovery Evaluator
              ↓
        Ranked Recovery Strategies
    """

    def __init__(self):

        self.evaluator = RecoveryEvaluator()

        self.generator = CandidatePlanGenerator()

        self.search = BeamSearchPlanner(
            evaluator=self.evaluator,
            beam_width=5,
        )

    # --------------------------------------------------

    def simulate(
        self,
        state,
        decisions,
    ):
        """
        Generate candidate recovery plans using Beam Search,
        evaluate each plan, and return the ranked simulations.
        """

        candidate_plans = self.search.search(
            state.tasks,
            state,
        )

        simulations = []

        for plan in candidate_plans:

            evaluation = self.evaluator.evaluate(
                tasks=plan,
                state=state,
            )

            simulations.append(
                {
                    "tasks": plan,
                    "evaluation": evaluation,
                }
            )

        simulations.sort(
            key=lambda simulation: simulation["evaluation"]["recovery_score"],
            reverse=True,
        )

        return simulations

    # --------------------------------------------------

    def best_strategy(
        self,
        state,
        decisions,
    ):
        """
        Returns the highest-scoring recovery strategy.
        """

        simulations = self.simulate(
            state,
            decisions,
        )

        if not simulations:
            return None

        return simulations[0]