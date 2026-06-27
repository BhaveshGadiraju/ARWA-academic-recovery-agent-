from models.state_vector import StudentState


class ReasoningEngine:
    """
    Synthesizes the outputs of every AI module into
    coherent reasoning that can be understood by users.
    """

    def generate_reasoning(
        self,
        state: StudentState,
        decisions,
    ):

        reasoning = []

        reasoning.append(
            self._academic_summary(state)
        )

        reasoning.append(
            self._burnout_summary(state)
        )

        reasoning.append(
            self._decision_summary(decisions)
        )

        reasoning.append(
            self._overall_strategy(state)
        )

        return reasoning

    # ------------------------------------

    def _academic_summary(
        self,
        state,
    ):

        prediction = state.academic_risk

        return (
            f"Academic risk is {prediction.level.lower()} "
            f"(score={prediction.score:.2f}). "
            f"The largest contributing factors are "
            f"{prediction.top_factors[0].factor} and "
            f"{prediction.top_factors[1].factor}."
        )

    # ------------------------------------

    def _burnout_summary(
        self,
        state,
    ):

        prediction = state.burnout_risk

        return (
            f"Burnout risk is {prediction.level.lower()} "
            f"(score={prediction.score:.2f}). "
            f"The largest contributors are "
            f"{prediction.top_factors[0].factor} and "
            f"{prediction.top_factors[1].factor}."
        )

    # ------------------------------------

    def _decision_summary(
        self,
        decisions,
    ):

        highest = decisions[0]

        return (
            f"The highest priority task is "
            f"{highest.task['name']} because "
            f"its recovery score "
            f"({highest.priority_score:.2f}) "
            f"is greater than all other tasks."
        )

    # ------------------------------------

    def _overall_strategy(
        self,
        state,
    ):

        academic = state.academic_risk.score
        burnout = state.burnout_risk.score

        if academic > burnout:

            return (
                "The recovery strategy prioritizes "
                "academic stabilization while "
                "maintaining manageable workload."
            )

        if burnout > academic:

            return (
                "The recovery strategy prioritizes "
                "burnout prevention while preserving "
                "important academic progress."
            )

        return (
            "The recovery strategy balances "
            "academic recovery with wellness."
        )