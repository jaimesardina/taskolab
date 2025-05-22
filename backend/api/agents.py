from fastapi import APIRouter, Depends
from core.security import authenticate_user
from core.mapper import get_mapper
import importlib

router = APIRouter()

@router.get("/mapper")
def agent_mapper(user=Depends(authenticate_user)):
    return get_mapper(user["role"])

@router.post("/exec-server")
def exec_server_task(data: dict, user=Depends(authenticate_user)):
    try:
        module_path = data.get("module")
        if not module_path:
            return {"error": "No module specified"}
            
        module = importlib.import_module(f"backend.modules.{module_path}")
        if hasattr(module, "main"):
            module.main()
            return {"result": "Task executed successfully"}
        else:
            return {"error": "Module has no main() function"}
            
    except ImportError as e:
        return {"error": f"Failed to import module: {str(e)}"}
    except Exception as e:
        return {"error": f"Error executing task: {str(e)}"}