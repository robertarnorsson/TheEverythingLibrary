import os

class TELEnviroment:
    '''
    ## Enviroment Variables
    ---
    This class provides utility functions for managing environment variables.

    **Note:** This class is a work in progress and subject to further development.
    '''
    
    def __init__(self):
        pass

    def set(self, name: str, value):
        '''
        ## Set Environment Variable
        ---
        ### Description
        Set the value of an environment variable.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.
            - `value`: The value to set for the environment variable.\n
        ---
        ### Exceptions
            - If an error occurs during setting the environment variable.\n
        '''
        try:
            os.environ[name] = value
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def get(self, name: str):
        '''
        ## Get Environment Variable
        ---
        ### Description
        Get the value of an environment variable.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.\n
        ---
        ### Return
            - The value of the environment variable, or `None` if not found.\n
        ---
        ### Exceptions
            - If an error occurs during retrieving the environment variable.\n
        '''
        try:
            return os.environ.get(name)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def remove(self, name: str):
        '''
        ## Remove Environment Variable
        ---
        ### Description
        Remove an environment variable.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.\n
        ---
        ### Exceptions
            - If an error occurs during removing the environment variable.\n
        '''
        try:
            if name in os.environ:
                del os.environ[name]
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def list_all(self):
        '''
        ## List All Environment Variables
        ---
        ### Description
        Retrieve a dictionary containing all environment variables and their values.\n
        ---
        ### Return
            - A dictionary containing all environment variables and their values.\n
        ---
        ### Exceptions
            - If an error occurs during retrieving the environment variables.\n
        '''
        try:
            return os.environ
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def exists(self, name: str):
        '''
        ## Check if Environment Variable Exists
        ---
        ### Description
        Check if an environment variable exists.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.\n
        ---
        ### Return
            - `True` if the environment variable exists, otherwise `False`.\n
        ---
        ### Exceptions
            - If an error occurs during checking the existence of the environment variable.\n
        '''
        try:
            return name in os.environ
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def get_multiple(self, names: list[str]):
        '''
        ## Get Multiple Environment Variables
        ---
        ### Description
        Get values of multiple environment variables.\n
        ---
        ### Arguments
            - `names`: A list of environment variable names.\n
        ---
        ### Return
            - A dictionary containing the requested environment variables and their values.\n
        ---
        ### Exceptions
            - If an error occurs during retrieving the environment variables.\n
        '''
        try:
            values = {}
            for name in names:
                values[name] = os.environ.get(name)
            return values
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def update(self, name: str, value):
        '''
        ## Update Environment Variable
        ---
        ### Description
        Update the value of an existing environment variable.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.
            - `value`: The new value to set for the environment variable.\n
        ---
        ### Exceptions
            - If an error occurs during updating the environment variable.\n
        '''
        try:
            if name in os.environ:
                os.environ[name] = value
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def append(self, name: str, value):
        '''
        ## Append to Environment Variable
        ---
        ### Description
        Append a value to an existing environment variable, separated by the appropriate path separator.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.
            - `value`: The value to append to the environment variable.\n
        ---
        ### Exceptions
            - If an error occurs during appending to the environment variable.\n
        '''
        try:
            if name in os.environ:
                current_value = os.environ[name]
                new_value = f"{current_value}{os.pathsep}{value}"
                os.environ[name] = new_value
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def prepend(self, name: str, value):
        '''
        ## Prepend to Environment Variable
        ---
        ### Description
        Prepend a value to an existing environment variable, separated by the appropriate path separator.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.
            - `value`: The value to prepend to the environment variable.\n
        ---
        ### Exceptions
            - If an error occurs during prepending to the environment variable.\n
        '''
        try:
            if name in os.environ:
                current_value = os.environ[name]
                new_value = f"{value}{os.pathsep}{current_value}"
                os.environ[name] = new_value
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def restore(self, name: str, original_value):
        '''
        ## Restore Environment Variable
        ---
        ### Description
        Restore an environment variable to its original value.\n
        ---
        ### Arguments
            - `name`: The name of the environment variable.
            - `original_value`: The original value to restore.\n
        ---
        ### Exceptions
            - If an error occurs during restoring the environment variable.\n
        '''
        try:
            os.environ[name] = original_value
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")