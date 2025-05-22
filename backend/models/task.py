from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    name: str
    description: str
    run_mode: str  # "local" or "server"
    module: str    # Python module path to execute
    roles: List[str]  # Roles allowed to access this task