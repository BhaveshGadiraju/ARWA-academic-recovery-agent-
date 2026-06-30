from models.strategy_comparison import RecoveryStrategy


class StrategyComparisonEngine:
    """
    Converts simulation results into three
    user-friendly recovery strategies.
    """

    def compare(
        self,
        simulations,
    ):

        if len(simulations) < 3:

            return []

        best = simulations[0]
        aggressive = simulations[1]
        wellness = simulations[2]

        strategies = [

            RecoveryStrategy(

                name="Balanced",

                projected_grade=best["evaluation"]["projected_grade"],

                recovery_score=best["evaluation"]["recovery_score"],

                recovery_probability=96,

                burnout=best["evaluation"]["burnout"],

                estimated_hours=best["evaluation"]["time_cost"],

                pros=[
                    "Highest recovery probability",
                    "Balanced workload",
                    "Lowest academic risk",
                ],

                cons=[
                    "Requires consistent study schedule",
                ],

                selected=True,
            ),

            RecoveryStrategy(

                name="Aggressive",

                projected_grade=aggressive["evaluation"]["projected_grade"],

                recovery_score=aggressive["evaluation"]["recovery_score"],

                recovery_probability=78,

                burnout=aggressive["evaluation"]["burnout"],

                estimated_hours=aggressive["evaluation"]["time_cost"],

                pros=[
                    "Maximum grade increase",
                ],

                cons=[
                    "Higher burnout",
                    "Less sustainable",
                ],
            ),

            RecoveryStrategy(

                name="Wellness",

                projected_grade=wellness["evaluation"]["projected_grade"],

                recovery_score=wellness["evaluation"]["recovery_score"],

                recovery_probability=90,

                burnout=wellness["evaluation"]["burnout"],

                estimated_hours=wellness["evaluation"]["time_cost"],

                pros=[
                    "Lowest burnout",
                    "Easy to maintain",
                ],

                cons=[
                    "Lower grade improvement",
                ],
            ),
        ]

        return strategies