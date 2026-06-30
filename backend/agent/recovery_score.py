from models.ai_report import AIReport


class ReportGenerator:
    """
    Generates ARWA's final AI report.

    This report is the single object returned to the
    frontend and contains the AI's complete analysis.
    """

    def generate(
        self,
        academic_prediction,
        burnout_prediction,
        recovery_score,
        forecast,
        strategies,
    ):

        # ------------------------------------------
        # Overall Confidence
        # ------------------------------------------

        confidence = round(
            (
                academic_prediction.confidence
                + burnout_prediction.confidence
            ) / 2,
            2,
        )

        # ------------------------------------------
        # Dynamic Insights
        # ------------------------------------------

        insights = []

        for factor in academic_prediction.top_factors:
            insights.append(
                f"{factor.factor} contributes {factor.contribution}% to academic risk."
            )

        for factor in burnout_prediction.top_factors:
            insights.append(
                f"{factor.factor} contributes {factor.contribution}% to burnout risk."
            )

        insights = insights[:5]

        # ------------------------------------------
        # Recommended Actions
        # ------------------------------------------

        actions = []

        if academic_prediction.level in ("HIGH", "CRITICAL"):
            actions.append(
                "Prioritize completing missing assignments immediately."
            )

        if burnout_prediction.level in ("HIGH", "CRITICAL"):
            actions.append(
                "Reduce workload and schedule recovery breaks."
            )

        actions.extend([

            "Follow the AI-recommended recovery strategy.",

            "Complete high-impact assignments before lower-value work.",

            "Review your progress daily and update the recovery plan."

        ])

        # Remove duplicates while preserving order
        actions = list(dict.fromkeys(actions))

        # ------------------------------------------
        # Executive Summary
        # ------------------------------------------

        summary = (
            f"ARWA predicts a "
            f"{recovery_score['after']['probability']}% probability "
            f"of successful academic recovery. "
            f"The Recovery Score is projected to improve from "
            f"{recovery_score['before']['score']} "
            f"to {recovery_score['after']['score']} "
            f"({recovery_score['improvement']} point improvement). "
            f"The recommended strategy balances academic performance "
            f"with burnout prevention while maximizing long-term success."
        )

        # ------------------------------------------
        # Final Report
        # ------------------------------------------

        return AIReport(

            recovery_score=recovery_score,

            academic_prediction=academic_prediction,

            burnout_prediction=burnout_prediction,

            forecast=forecast,

            strategies=strategies,

            top_insights=insights,

            recommended_actions=actions,

            executive_summary=summary,

            confidence=confidence,

        )