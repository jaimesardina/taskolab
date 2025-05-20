def get_mapper(role):
    match role:
        case "operator":
            return {
                "entry_type": "network_diagnostics_tool",
                "module": "network_diagnostics_tool.initial",
                "description": f"Welcome {role}, This tool will help you diagnose network issues.\n"
            }
        case "support":
            return {
                "entry_type": "network_diagnostics_tool",
                "module": "network_diagnostics_tool.initial",
                "description": "Welcome support, This tool will help you diagnose network issues.\n"
            }
        case "admin":
            return {
                "entry_type": "network_diagnostics_tool",
                "module": "network_diagnostics_tool.initial",
                "description": "Welcome admin, This tool will help you diagnose network issues.\n"
            }