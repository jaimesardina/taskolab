from fastapi import APIRouter, Depends
from core.security import authenticate_user
from models.task import Task

router = APIRouter()

@router.get("/", dependencies=[Depends(authenticate_user)])
def list_tasks():
    return [
        Task(id="ping_vendor", name="Ping Vendor Devices", description="Ping all vendor devices", run_mode="run_locally"),
        Task(id="check_arp", name="Check ARP Table", description="Get ARP info from firewall", run_mode="run_on_server")
    ]

@router.post("/{task_id}/resolve", dependencies=[Depends(authenticate_user)])
def resolve_task(task_id: str):
    return {"task_id": task_id, "payload": "encrypted-command-placeholder"}