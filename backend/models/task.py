from pydantic import BaseModel

class Task(BaseModel):
    id: int
    name: str
    description: str
    run_mode: str  # "run_locally" or "run_on_server"