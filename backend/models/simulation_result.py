from dataclasses import dataclass


@dataclass
class SimulationResult:
    """
    Represents the predicted outcome of
    a recovery strategy.
    """

    strategy: str

    predicted_grade: float

    predicted_burnout: float

    recovery_score: float

    explanation: str