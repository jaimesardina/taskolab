from fastapi import APIRouter, Depends
from core.security import authenticate_user
from core.mapper import get_mapper

router = APIRouter()

@router.get("/mapper")
def agent_mapper(user=Depends(authenticate_user)):
    
    return get_mapper(user["role"])
