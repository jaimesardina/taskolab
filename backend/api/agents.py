from fastapi import APIRouter, Depends
from core.security import authenticate_user
from core.mapper import get_mapper

router = APIRouter()

@router.get("/mapper", dependencies=[Depends(authenticate_user)])
def agent_mapper():
    return get_mapper()
