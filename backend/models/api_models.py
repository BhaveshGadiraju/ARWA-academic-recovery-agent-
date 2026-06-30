from pydantic import BaseModel


class AssignmentRequest(BaseModel):

    title: str

    course: str

    difficulty: float

    estimated_hours: float

    days_remaining: int

    completed: bool


class StudentRequest(BaseModel):

    current_grade: float

    stress_level: float

    available_time: float

    assignments: list[AssignmentRequest]