from agent.recovery_orchestrator import RecoveryOrchestrator


class RecoveryController:

    def __init__(self):

        self.agent = RecoveryOrchestrator()

    def analyze(

        self,

        student_data,

    ):

        return self.agent.run(

            student_data,

        )