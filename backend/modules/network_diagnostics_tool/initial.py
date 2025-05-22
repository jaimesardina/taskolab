import sys
from pathlib import Path
from backend.modules.network_diagnostics_tool.ping_test import run_logic

# Ensure the current directory is in the system path
sys.path.append(str(Path(__file__).resolve().parent.parent))
def main():
    print("Welcome to the Network Diagnostics Tool!")
    print("This tool will help you diagnose network issues.\n")
    usr_response = input("Choose a task: \n1. Ping Test \n2. Traceroute\n")
    run_logic(usr_response)

if __name__ == "__main__":
    main()

    