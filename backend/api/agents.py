from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TaskReport(BaseModel):
    task_id: int
    agent_id: str
    result: str

@router.post("/report")
def report_task_execution(report: TaskReport):
    print("[LOG]", report)
    return {"status": "received"}