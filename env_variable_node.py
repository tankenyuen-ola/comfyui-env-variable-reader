import os
from dotenv import load_dotenv
import folder_paths

class EnvironmentVariableNode:
    """
    A ComfyUI custom node that reads environment variables from a .env file
    and allows selection of specific variables to output their values.
    """
    
    def __init__(self):
        # Load environment variables from .env file in ComfyUI directory
        env_path = os.path.join(folder_paths.base_path, '.env')
        if os.path.exists(env_path):
            load_dotenv(env_path)
    
    @classmethod
    def INPUT_TYPES(cls):
        # Get available environment variables from .env file
        env_vars = cls.get_env_variables()
        
        return {
            "required": {
                "env_variable": (env_vars, {"default": env_vars[0] if env_vars else ""}),
            }
        }
    
    @classmethod
    def get_env_variables(cls):
        """Read and parse .env file to get available environment variable names"""
        env_path = os.path.join(folder_paths.base_path, '.env')
        env_vars = []
        
        if os.path.exists(env_path):
            try:
                with open(env_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        line = line.strip()
                        # Skip empty lines and comments
                        if line and not line.startswith('#'):
                            # Split on first '=' to get variable name
                            if '=' in line:
                                var_name = line.split('=', 1)[0].strip()
                                if var_name:
                                    env_vars.append(var_name)
            except Exception as e:
                print(f"Error reading .env file: {e}")
        
        # Return at least one option to prevent errors
        return env_vars if env_vars else ["NO_ENV_VARS_FOUND"]
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("env_value",)
    FUNCTION = "get_env_value"
    CATEGORY = "utils"
    DESCRIPTION = "Read environment variables from .env file and output selected variable value"
    
    def get_env_value(self, env_variable):
        """Get the value of the selected environment variable"""
        if env_variable == "NO_ENV_VARS_FOUND":
            return ("No .env file found or no variables available",)
        
        # Get the environment variable value
        env_value = os.getenv(env_variable, "")
        
        if not env_value:
            # If not found in environment, try reading directly from .env file
            env_path = os.path.join(folder_paths.base_path, '.env')
            if os.path.exists(env_path):
                try:
                    with open(env_path, 'r', encoding='utf-8') as file:
                        for line in file:
                            line = line.strip()
                            if line and not line.startswith('#'):
                                if '=' in line:
                                    var_name, var_value = line.split('=', 1)
                                    var_name = var_name.strip()
                                    var_value = var_value.strip()
                                    
                                    # Remove quotes if present
                                    if var_value.startswith('"') and var_value.endswith('"'):
                                        var_value = var_value[1:-1]
                                    elif var_value.startswith("'") and var_value.endswith("'"):
                                        var_value = var_value[1:-1]
                                    
                                    if var_name == env_variable:
                                        env_value = var_value
                                        break
                except Exception as e:
                    print(f"Error reading .env file: {e}")
                    return (f"Error reading environment variable: {e}",)
        
        return (env_value,)

# Node mapping for ComfyUI
NODE_CLASS_MAPPINGS = {
    "EnvironmentVariableNode": EnvironmentVariableNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EnvironmentVariableNode": "Environment Variable Reader"
}