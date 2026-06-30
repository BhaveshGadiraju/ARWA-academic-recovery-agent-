from agent.feature_extractor import FeatureExtractor
from agent.decision_engine import DecisionEngine
from agent.reasoning_engine import ReasoningEngine
from agent.reflection_engine import ReflectionEngine
from agent.planner import Planner
from agent.explanation_engine import ExplanationEngine
from agent.experience_memory import ExperienceMemory
from agent.simulation_engine import SimulationEngine
from agent.recovery_score import RecoveryScoreEngine
from agent.recovery_forecast import RecoveryForecastEngine
from agent.strategy_comparison import StrategyComparisonEngine

from models.academic_risk_model import AcademicRiskModel
from models.burnout_risk_model import BurnoutRiskModel
from models.state_vector import StateVectorBuilder


class RecoveryOrchestrator:
    """
    Master AI pipeline for ARWA.

    Coordinates feature extraction, prediction,
    planning, simulation, reasoning, explainability,
    forecasting, and memory.
    """

    def __init__(self):

        self.feature_extractor = FeatureExtractor()

        self.academic_model = AcademicRiskModel()

        self.burnout_model = BurnoutRiskModel()

        self.state_builder = StateVectorBuilder()

        self.decision_engine = DecisionEngine()

        self.planner = Planner()

        self.reasoning_engine = ReasoningEngine()

        self.reflection_engine = ReflectionEngine()

        self.explanation_engine = ExplanationEngine()

        self.memory = ExperienceMemory()

        self.simulation_engine = SimulationEngine()

        self.recovery_score = RecoveryScoreEngine()

        self.recovery_forecast = RecoveryForecastEngine()

        self.strategy_comparison = StrategyComparisonEngine()

    # --------------------------------------------------

    def run(
        self,
        student_data,
    ):

        # ----------------------------------------------
        # Phase 1
        # Feature Extraction
        # ----------------------------------------------

        features = self.feature_extractor.extract(
            student_data
        )

        # ----------------------------------------------
        # Phase 2
        # AI Prediction
        # ----------------------------------------------

        academic_prediction = self.academic_model.predict(
            features
        )

        burnout_prediction = self.burnout_model.predict(
            features
        )

        # ----------------------------------------------
        # Phase 3
        # State Construction
        # ----------------------------------------------

        state = self.state_builder.build(

            features=features,

            academic_prediction=academic_prediction,

            burnout_prediction=burnout_prediction,

            tasks=student_data.tasks,

        )

        # ----------------------------------------------
        # Phase 4
        # Decision Making
        # ----------------------------------------------

        decisions = self.decision_engine.optimize(
            state
        )

        # ----------------------------------------------
        # Phase 5
        # Planning
        # ----------------------------------------------

        plan = self.planner.generate(
            decisions
        )

        # ----------------------------------------------
        # Phase 6
        # Simulation
        # ----------------------------------------------

        simulations = self.simulation_engine.simulate(
            state,
            decisions,
        )

        strategies = self.strategy_comparison.compare(
            simulations
        )

        best_strategy = self.simulation_engine.best_strategy(
            state,
            decisions,
        )

        # ----------------------------------------------
        # Phase 7
        # Recovery Score
        # ----------------------------------------------

        current_score = self.recovery_score.calculate_current(
            state,
        )

        projected_score = self.recovery_score.calculate_projected(
            state,
            best_strategy,
        )

        recovery_score = self.recovery_score.calculate_improvement(
            current_score,
            projected_score,
        )

        # ----------------------------------------------
        # Phase 8
        # Forecast
        # ----------------------------------------------

        forecast = self.recovery_forecast.forecast(

            state,

            best_strategy,

            recovery_score["after"],

        )

        # ----------------------------------------------
        # Phase 9
        # Explainability
        # ----------------------------------------------

        reasoning = self.reasoning_engine.generate_reasoning(
            state,
            decisions,
        )

        explanations = self.explanation_engine.generate(
            decisions
        )

        # ----------------------------------------------
        # Phase 10
        # Reflection
        # ----------------------------------------------

        reflection = self.reflection_engine.reflect(
            state,
            decisions,
        )

        # ----------------------------------------------
        # Phase 11
        # Memory
        # ----------------------------------------------

        self.memory.store(

            state=state,

            decisions=decisions,

            reflection=reflection,

        )

        # ----------------------------------------------
        # Final AI Output
        # ----------------------------------------------

        return {

            "features": features,

            "academic_prediction": academic_prediction,

            "burnout_prediction": burnout_prediction,

            "state": state,

            "decisions": decisions,

            "plan": plan,

            "reasoning": reasoning,

            "explanations": explanations,

            "reflection": reflection,

            "simulations": simulations,

            "best_strategy": best_strategy,

            "recovery_score": recovery_score,

            "forecast": forecast,

            "strategies": strategies,

        }