from dataclasses import dataclass
from typing import List, Any


@dataclass
class AIReport:

    recovery_score: Any

    academic_prediction: Any

    burnout_prediction: Any

    forecast: List

    strategies: List

    top_insights: List[str]

    recommended_actions: List[str]

    executive_summary: str

    confidence: float
    