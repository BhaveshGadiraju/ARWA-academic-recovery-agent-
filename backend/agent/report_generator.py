from models.ai_report import AIReport


class ReportGenerator:
    """
    Creates ARWA's final AI report.

    This object is sent directly to the frontend.
    """

    def generate(

        self,

        academic_prediction,

        burnout_prediction,

        recovery_score,

        forecast,

        strategies,

    ):

        confidence = round(

            (

                academic_prediction.confidence

                +

                burnout_prediction.confidence

            ) / 2,

            2,

        )

        insights = [

            "Missing assignments have the greatest impact on academic recovery.",

            "Balanced Strategy provides the highest recovery probability.",

            "Completing high-value assignments first maximizes grade improvement.",

        ]

        actions = [

            "Complete the highest-priority assignment today.",

            "Reserve uninterrupted study blocks.",

            "Monitor workload to avoid burnout.",

        ]

        summary = (

            f"ARWA predicts a "

            f"{recovery_score['after']['probability']}% "

            f"chance of successful academic recovery "

            f"if the recommended strategy is followed."

        )

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