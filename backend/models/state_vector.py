from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class StudentState:
    """
    Unified memory object for ARWA.
    Contains EVERYTHING the agent currently knows.
    """

    # Raw extracted features
    features: Dict[str, Any]

    # AI model outputs
    academic_risk: Any
    burnout_risk: Any

    # Core student context
    tasks: List[Dict]

    available_time: float
    current_grade: float
    stress_level: float


class StateVectorBuilder:
    """
    Converts raw pipeline outputs into a unified state object.
    """

    def build(
        self,
        features: Dict,
        academic_prediction,
        burnout_prediction,
        tasks: List[Dict]
    ) -> StudentState:

        return StudentState(

            features=features,

            academic_risk=academic_prediction,

            burnout_risk=burnout_prediction,

            tasks=tasks,

            available_time=features.get("available_time", 0),

            current_grade=features.get("current_grade", 0),

            stress_level=features.get("stress_level", 0)
        )