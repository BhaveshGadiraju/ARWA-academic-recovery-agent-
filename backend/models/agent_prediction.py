from dataclasses import dataclass, field
from typing import List


@dataclass
class ContributingFactor:
    """
    Represents one factor that contributed to an AI prediction.
    """

    factor: str
    contribution: float
    explanation: str


@dataclass
class AgentPrediction:
    """
    Standard prediction object returned by every AI model in ARWA.
    """

    score: float

    level: str

    confidence: float

    top_factors: List[ContributingFactor] = field(default_factory=list)

    reasoning: List[str] = field(default_factory=list)