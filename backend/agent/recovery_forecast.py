class RecoveryForecastEngine:
    """
    Predicts how the student's academic state changes
    over the next several days if they follow the
    recommended recovery strategy.
    """

    def forecast(
        self,
        state,
        strategy,
        recovery_score,
        days=5,
    ):

        forecast = []

        current_grade = state.current_grade

        burnout = state.burnout_risk.score

        probability = recovery_score["probability"]

        grade_gain = strategy["evaluation"]["grade_gain"]

        burnout_cost = strategy["evaluation"]["burnout"]

        total_tasks = len(state.tasks)

        remaining_tasks = total_tasks

        grade_step = grade_gain / days

        burnout_step = burnout_cost / days

        completed_step = max(
            1,
            round(total_tasks / days),
        )

        for day in range(1, days + 1):

            current_grade += grade_step

            burnout = max(
                0,
                burnout - burnout_step * 0.25,
            )

            remaining_tasks = max(
                0,
                remaining_tasks - completed_step,
            )

            forecast.append(

                {

                    "day": day,

                    "predicted_grade": round(
                        current_grade,
                        1,
                    ),

                    "predicted_burnout": round(
                        burnout,
                        2,
                    ),

                    "remaining_tasks": remaining_tasks,

                    "recovery_probability": probability,

                }

            )

        return forecast