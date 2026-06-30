from dataclasses import dataclass
from typing import List


@dataclass
class RecoveryStrategy:

    name: str

    projected_grade: float

    recovery_score: int

    recovery_probability: int

    burnout: float

    estimated_hours: float

    pros: List[str]

    cons: List[str]

    selected: bool = False
    