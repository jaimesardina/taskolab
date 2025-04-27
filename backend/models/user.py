from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str  # Note: store hashed in a real DB!
    role: str = "developer"  # e.g., developer, support, admin