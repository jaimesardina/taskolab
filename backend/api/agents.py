from fastapi import APIRouter, HTTPException, Depends
from core.security import authenticate_user
from core.mapper import get_mapper
import importlib
import sys
from io import StringIO
import contextlib


router = APIRouter()

@router.get("/mapper")
def agent_mapper(user=Depends(authenticate_user)):
    return get_mapper(user["role"])

@router.post("/exec-server")
def exec_server_task(data: dict, user=Depends(authenticate_user)):
    try:
        module_path = data.get("module")
        user_input = data.get("input")
        
        if not module_path:
            raise HTTPException(status_code=400, detail="No module specified")

        output = StringIO()
        with contextlib.redirect_stdout(output):
            module = importlib.import_module(f"backend.modules.{module_path}")
            if hasattr(module, "main"):  # Changed from run_logic to main
                result = module.main(user_input)
                
                # If the module returns a dict with requires_input
                if isinstance(result, dict) and result.get("requires_input"):
                    return {
                        "status": "success",
                        "output": output.getvalue(),
                        "requires_input": True,
                        "prompt": result.get("prompt", "Enter your choice: ")
                    }
                
            else:
                raise HTTPException(status_code=400, detail="Module has no main() function")

        return {
            "status": "success",
            "output": output.getvalue(),
            "result": "Task executed successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing task: {str(e)}")