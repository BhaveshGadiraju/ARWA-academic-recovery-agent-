from fastapi import APIRouter, HTTPException

from api.controller import RecoveryController
from models.api_models import StudentRequest

router = APIRouter()

controller = RecoveryController()


@router.get("/")
def home():

    return {

        "message": "ARWA AI Backend",

        "status": "running",

        "version": "1.0",

    }


@router.get("/health")
def health():

    return {

        "status": "healthy",

        "agent": "RecoveryOrchestrator",

    }


@router.post("/analyze")
def analyze(student: StudentRequest):

    try:

        result = controller.analyze(student)

        return result

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e),

        )