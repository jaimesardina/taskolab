import sys
from pathlib import Path
from backend.modules.network_diagnostics_tool.ping_test import run_logic as execute_ping_test

# Ensure the current directory is in the system path
sys.path.append(str(Path(__file__).resolve().parent.parent))

def main(user_input=None):
    """Main entry point that supports both interactive and server modes"""
    print("Welcome to the Network Diagnostics Tool!")
    print("This tool will help you diagnose network issues.\n")
    
    if user_input is None:
        # For server-side execution, return the prompt
        return {
            "requires_input": True,
            "prompt": "Choose a task:\n1. Ping Test\n2. Traceroute\n"
        }
    
    # Execute the selected task
    return execute_ping_test(user_input)

if __name__ == "__main__":
    # For local testing, run interactively
    response = main()
    if response.get("requires_input"):
        user_choice = input(response.get("prompt"))
        main(user_choice)