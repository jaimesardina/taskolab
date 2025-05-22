from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    name: str
    description: str
    run_mode: str  # "run_locally" or "run_on_server"
    module: str    # Python module path to execute
    roles: List[str]  # Roles allowed to access this task