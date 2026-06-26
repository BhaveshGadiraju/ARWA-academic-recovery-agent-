from typing import Dict

from models.agent_prediction import (
    AgentPrediction,
    ContributingFactor
)


class AcademicRiskModel:
    """
    Predicts the student's academic risk using
    engineered features from the FeatureExtractor.
    """

    def __init__(self):

        self.weights = {
            "missing_tasks": 0.30,
            "current_grade": 0.30,
            "deadline_density": 0.15,
            "estimated_workload": 0.15,
            "average_difficulty": 0.10
        }

    def normalize_grade(self, grade):
        return max(0.0, min(1.0, (100 - grade) / 100))

    def normalize_missing_tasks(self, missing_tasks):
        return min(missing_tasks / 10, 1.0)

    def normalize_workload(self, workload):
        return min(workload / 20, 1.0)

    def normalize_difficulty(self, difficulty):
        return difficulty / 10

    def normalize_deadline_density(self, density):
        return min(density, 1.0)

    def classify_risk(self, score):

        if score >= 0.80:
            return "CRITICAL"
        if score >= 0.60:
            return "HIGH"
        if score >= 0.40:
            return "MEDIUM"
        return "LOW"

    def calculate_confidence(self, features):

        completeness = sum(
            value is not None
            for value in features.values()
        )

        return round(completeness / len(features), 2)

    def predict(self, features: Dict):

        grade = self.normalize_grade(features["current_grade"])
        missing = self.normalize_missing_tasks(features["missing_tasks"])
        workload = self.normalize_workload(features["estimated_workload"])
        difficulty = self.normalize_difficulty(features["average_difficulty"])
        density = self.normalize_deadline_density(features["deadline_density"])

        risk_score = (
            grade * self.weights["current_grade"]
            + missing * self.weights["missing_tasks"]
            + workload * self.weights["estimated_workload"]
            + density * self.weights["deadline_density"]
            + difficulty * self.weights["average_difficulty"]
        )

        risk_level = self.classify_risk(risk_score)
        confidence = self.calculate_confidence(features)

        # -------------------------
        # Explainability
        # -------------------------
        top_factors = [
            ContributingFactor(
                factor="Missing Assignments",
                contribution=round(
                    missing * self.weights["missing_tasks"] * 100,
                    1
                ),
                explanation="Multiple missing assignments increase academic risk."
            ),
            ContributingFactor(
                factor="Current Grade",
                contribution=round(
                    grade * self.weights["current_grade"] * 100,
                    1
                ),
                explanation="Lower grades indicate a higher likelihood of academic decline."
            ),
            ContributingFactor(
                factor="Workload",
                contribution=round(
                    workload * self.weights["estimated_workload"] * 100,
                    1
                ),
                explanation="Heavy workload increases academic recovery difficulty."
            )
        ]

        reasoning = [
            f"Overall academic risk classified as {risk_level}.",
            "Risk is computed from normalized academic features.",
            "Missing assignments and current grade are the strongest indicators."
        ]

        return AgentPrediction(
            score=round(risk_score, 2),
            level=risk_level,
            confidence=confidence,
            top_factors=top_factors,
            reasoning=reasoning
        )