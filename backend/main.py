# This ensures that when main.py runs, it can locate sibling folders like api, core, models.
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import auth, tasks, agents


app = FastAPI(title="SupportOps API")

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(tasks.router, prefix="/tasks")
app.include_router(agents.router, prefix="/agent")


@app.get("/")
def root():
    return {"message": "SupportOps API is running"}