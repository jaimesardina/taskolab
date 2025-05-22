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

    def execute_server_task(self, module_path: str, token: str, user_input: str = None):
        headers = {"Authorization": f"Bearer {token}"}
        data = {
            "module": module_path,
            "input": user_input
        }
        
        try:
            print(f"Executing server task... {'with input: ' + user_input if user_input else ''}")
            response = requests.post(
                f"{self.api_base_url}/agent/exec-server",
                json=data,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get("output"):
                    print("\nServer Output:")
                    print(result.get("output"))
                
                # Handle interactive prompts
                if result.get("requires_input"):
                    user_input = input(result.get("prompt", "Enter your choice: "))
                    return self.execute_server_task(module_path, token, user_input)
                    
            else:
                print(f"Server error: {response.text}")
                
        except requests.Timeout:
            print("Request timed out after 10 seconds")
        except requests.RequestException as e:
            print(f"Error communicating with server: {str(e)}")

    def run_logic(self, module):  # Changed from user_input=None to self, module
        try:
            if hasattr(module, "main"):
                response = module.main()
                if response and response.get("requires_input"):
                    user_input = input(response.get("prompt", "Enter your choice: "))
                    module.main(user_input)
            else:
                print("Module has no main() function")
        except Exception as e:
            print(f"Error executing module: {str(e)}")

    def run(self):
        """Main execution loop for the CLI agent"""
        try:
            # Initialize session
            token = self.login()
            mapper_data = self.fetch_mapper(token)
            tasks = mapper_data.get("tasks", [])

            if not tasks:
                print("No tasks available.")
                return

            # Display available tasks
            print("\nAvailable Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task['name']} ({task['run_mode']}) - {task['description']}")

            # Get user selection
            choice = input("\nSelect task (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Exiting...")
                return

            try:
                selected_task = tasks[int(choice) - 1]
            except (IndexError, ValueError):
                print("Invalid selection.")
                return

            # Execute task based on run mode
            module_path = selected_task["module"]
            run_mode = selected_task["run_mode"]

            if run_mode == "local":
                module = self.dynamic_import(module_path)
                self.run_logic(module)
            elif run_mode == "server":
                print("Sending request to server...")
                self.execute_server_task(module_path, token)
            else:
                print(f"Unsupported run mode: {run_mode}")

        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    cli = TaskolabCLI(api_base_url="http://127.0.0.1:8000")
    cli.run()
