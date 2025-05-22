import requests
import importlib
import getpass
import sys
import os

class TaskolabCLI:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
        sys.path.append(os.path.join(os.path.dirname(__file__), ''))

    def login(self):
        print("\nLogin to Taskolab\n")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        response = requests.post(f"{self.api_base_url}/auth/login", json={
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

    def fetch_mapper(self, token):
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{self.api_base_url}/agent/mapper", headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch mapper.")
            sys.exit(1)

    def dynamic_import(self, module_path):
        try:
            module = importlib.import_module(f"backend.modules.{module_path}")
            return module
        except ImportError:
            print(f"Failed to import logic module: {module_path}")
            sys.exit(1)

    def run_logic(self, module):
        if hasattr(module, "main"):
            module.main()
        else:
            print(f"The logic module {module} does not have a 'main' function.")
            sys.exit(1)

    def run(self):
        token = self.login()
        mapper_data = self.fetch_mapper(token)
        tasks = mapper_data.get("tasks", [])

        if not tasks:
            print("No tasks available.")
            return

        # Display menu
        print("\nAvailable Modules:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['name']} ({task['run_mode']}) - {task['description']}")

        choice = input("\nSelect task to import: ")
        try:
            selected_task = tasks[int(choice) - 1]
        except (IndexError, ValueError):
            print("Invalid selection.")
            return

        module_path = selected_task["module"]
        run_mode = selected_task["run_mode"]

        if run_mode == "local":
            module = self.dynamic_import(module_path)
            self.run_logic(module)
        elif run_mode == "server":
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.post(
                f"{self.api_base_url}/agent/exec-server",
                json={"module": module_path},
                headers=headers
            )
            print("Server response:", response.text)
        else:
            print("Unknown run mode.")

if __name__ == "__main__":
    cli = TaskolabCLI(api_base_url="http://127.0.0.1:8000")
    cli.run()
