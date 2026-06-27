from typing import List


class ReflectionEngine:
    """
    Reviews the generated recovery plan and provides
    feedback about its quality and potential improvements.
    """

    def reflect(self, state, decisions):

        reflection = {
            "summary": "",
            "strengths": [],
            "warnings": [],
            "recommendations": [],
        }

        reflection["summary"] = self._generate_summary(
            state,
            decisions,
        )

        reflection["strengths"] = self._identify_strengths(
            state,
            decisions,
        )

        reflection["warnings"] = self._identify_warnings(
            state,
            decisions,
        )

        reflection["recommendations"] = self._generate_recommendations(
            state,
            decisions,
        )

        return reflection

    # --------------------------------------------------

    def _generate_summary(
        self,
        state,
        decisions,
    ):

        return (
            f"Generated a recovery plan with "
            f"{len(decisions)} prioritized tasks."
        )

    # --------------------------------------------------

    def _identify_strengths(
        self,
        state,
        decisions,
    ):

        strengths = []

        if decisions:
            strengths.append(
                "Tasks were successfully prioritized."
            )

        if state.academic_risk.score < 0.60:
            strengths.append(
                "Academic risk is currently manageable."
            )

        if state.burnout_risk.score < 0.60:
            strengths.append(
                "Burnout risk remains under control."
            )

        return strengths

    # --------------------------------------------------

    def _identify_warnings(
        self,
        state,
        decisions,
    ):

        warnings = []

        if state.academic_risk.score >= 0.80:
            warnings.append(
                "Critical academic risk detected."
            )

        if state.burnout_risk.score >= 0.80:
            warnings.append(
                "Critical burnout risk detected."
            )

        high_priority = [
            d for d in decisions
            if d.priority_score >= 8
        ]

        if len(high_priority) >= 5:
            warnings.append(
                "Large number of urgent tasks."
            )

        return warnings

    # --------------------------------------------------

    def _generate_recommendations(
        self,
        state,
        decisions,
    ):

        recommendations = []

        if state.burnout_risk.score > state.academic_risk.score:
            recommendations.append(
                "Schedule recovery breaks between study sessions."
            )

        if state.academic_risk.score > 0.70:
            recommendations.append(
                "Prioritize assignments with the highest grade impact."
            )

        if len(decisions) > 8:
            recommendations.append(
                "Focus only on the top priorities today."
            )

        return recommendations