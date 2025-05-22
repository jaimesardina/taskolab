from core.tasks import TASKS

def get_mapper(role):
    return {
        "tasks": [
            task for task in TASKS if role in task["roles"]
        ]
    }