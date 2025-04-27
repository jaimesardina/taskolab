import requests
import importlib
import getpass
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ''))

API_BASE_URL = "http://127.0.0.1:8000"  # Update to your backend server if needed

def login():
    print("\nLogin to Taskolab\n")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    response = requests.post(f"{API_BASE_URL}/auth/login", json={
        "username": username,
        "password": password
    })

    if response.status_code == 200:
        token = response.json()["access_token"]
        print("Login successful")
        return token
    else:
        print("Login failed. Check credentials.")
        sys.exit(1)

def fetch_mapper(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{API_BASE_URL}/agent/mapper", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch mapper.")
        sys.exit(1)

def dynamic_import(module_path):
    try:
        module = importlib.import_module(f"backend.logic_templates.{module_path}")
        return module
    except ImportError:
        print(f"Failed to import logic module: {module_path}")
        sys.exit(1)

def run_logic(module):
    if hasattr(module, "main"):
        module.main()
    else:
        print(f"The logic module {module} does not have a 'main' function.")
        sys.exit(1)

def main():
    token = login()
    mapper_data = fetch_mapper(token)

    entry_type = mapper_data.get("entry_type")
    module_path = mapper_data.get("module")
    description = mapper_data.get("description")

    print(f"\n{description}\n")

    module = dynamic_import(module_path)
    run_logic(module)

if __name__ == "__main__":
    main()
