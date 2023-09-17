import os
import argon2
import hashlib
import base64

class TELHash:
    '''
    ## Hash
    ---
    This class provides utility functions for generating salt and pepper, hash passwords, and hash verification.

    **Note:** This class uses the Argon2 password hashing algorithm for secure password storage.
    '''

    def __init__(self):
        pass

    @staticmethod
    def generate_salt(length: int = 16) -> str:
        '''
        ## Generate salt
        ---
        Generates a random salt for password hashing.\n
        ---
        ### Arguments:
            - `length` (optional): The length of the generated salt in bytes (default is `16`).\n
        ---
        ### Returns:
            - The randomly generated salt in hexadecimal format.\n
        '''
        try:
            salt = os.urandom(length).hex()
            return salt
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    @staticmethod
    def hash(password: str, salt: str, pepper: str | None = None, encode_hash: bool = True, params: dict | None = None) -> str:
        '''
        ## Hash password
        ---
        Hashes a password using Argon2 with a given salt and pepper.\n
        ---
        ### Arguments:
            - `password`: The password to be hashed.\n
            - `salt`: The salt used for password hashing.\n
            - `pepper` (optional): The pepper used for password hashing (default is `None`).\n
            - `encode_hash` (optional): Should the hash be further encoded with url safe base64 encoding (default is `True`).\n
            - `params` (optional): Additional parameters for the hashing function (default is `None`).\n
            **Note**: Do NOT use params if you don't know what you are doing!\n
            Available parameters\n
            ```python
            params = {
                "hash_len": 80,
                "salt_len": 16,
                "time_cost": 10,
                "memory_cost": 2**12,
                "parallelism": 6,
                "encoding": 'ascii'
            }
            ```
        ---
        ### Returns:
            - The hashed password.\n
        '''
        try:
            password = f"{salt}{password}"
            password = password if pepper is None else f"{password}{pepper}"

            default_params = {
                "hash_len": 80,
                "salt_len": len(salt),
                "time_cost": 10,
                "memory_cost": 2**12,
                "parallelism": 6,
                "encoding": 'ascii'
            }

            keys_to_remove = []
            for key in params.keys():
                if key not in default_params:
                    keys_to_remove.append(key)

            for key in keys_to_remove:
                del params[key]

            default_params.update(params)

            hasher = argon2.PasswordHasher(**default_params)

            password = f"{password}{''.join([f'{value}' for _, value in default_params.items()])}"
            
            hashed_password = hasher.hash(password)
            
            return hashed_password if not encode_hash else base64.urlsafe_b64encode(base64.a85encode(hashed_password.encode())).decode()
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    @staticmethod
    def verify(hashed_password: str, password: str, salt: str, pepper: str | None = None, params: dict | None = None, raise_error: bool = False, return_reason: bool = False) -> bool:
        '''
        ## Verify hash
        ---
        Verifies a password against its hashed version using Argon2 with the provided salt and pepper.\n
        ---
        ### Arguments:
            - `hashed_password`: The previously hashed password.\n
            - `password`: The password to be verified.\n
            - `salt`: The salt used for password hashing.\n
            - `pepper` (optional): The pepper used for password hashing.\n
            - `params` (optional): Additional parameters for the hashing function (default is `None`).\n
            - `raise_error` (optional): Should the function raise an error if the hashes does not match (default is `False`).\n
            - `return_reason` (optional): Should the function return a reason with the result (default is `False`).\n
        ---
        ### Returns:
            - True if the password is valid, False otherwise (if `raise_error` is false).\n
        ---
        ### Exceptions
            - If verification failed, the hash is invalid or an error occurs during verification.\n
        '''
        try:
            password = f"{salt}{password}"
            password = password if pepper is None else f"{password}{pepper}"

            default_params = {
                "hash_len": 80,
                "salt_len": len(salt),
                "time_cost": 10,
                "memory_cost": 2**12,
                "parallelism": 6,
                "encoding": 'ascii'
            }

            keys_to_remove = []
            for key in params.keys():
                if key not in default_params:
                    keys_to_remove.append(key)

            for key in keys_to_remove:
                del params[key]

            default_params.update(params)

            hasher = argon2.PasswordHasher(**default_params)

            password = f"{password}{''.join([f'{value}' for _, value in default_params.items()])}"

            hashed_password = base64.a85decode(base64.urlsafe_b64decode(hashed_password.encode())).decode()

            hasher.verify(hashed_password, password)
            return True if not return_reason else {"return": True, "reason": "Verification success"}
        except argon2.exceptions.VerificationError as e:
            if not raise_error:
                return False if not return_reason else {"return": False, "reason": "Verification failed"}
            else:
                raise argon2.exceptions.VerificationError(f"Verification failed: {e}")
        except argon2.exceptions.InvalidHash as e:
            if not raise_error:
                return False if not return_reason else {"return": False, "reason": "The hash is an invalid hash"}
            else:
                raise argon2.exceptions.InvalidHash(f"The hash is an invalid hash: {e}")
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    @staticmethod
    def hash_file(file: str, algorithm: str = 'sha256', as_upper: bool = False) -> str:
        '''
        ## Hash File
        ---
        Calculates the hash of a file for integrity checks using a specified algorithm (default is `SHA-256`).\n
        ---
        ### Arguments:
            - `file`: The path to the file to be hashed.\n
            - `algorithm` (optional): The hashing algorithm to use (default is `sha256`). Supported algorithms: `sha1`, `sha256`, `sha384`, `sha512`, `md5`.\n
            - `as_upper` (optional): Should return hash in upper case (default is `False`).\n
        ---
        ### Returns:
            - The hash of the file in hexadecimal format.\n
        ---
        ### Exceptions:
            - If an error occurs during file reading or hashing or an error occurs something else.\n
        '''
        try:
            if algorithm == 'sha1':
                hash_object = hashlib.sha1()
            elif algorithm == 'sha256':
                hash_object = hashlib.sha256()
            elif algorithm == 'sha384':
                hash_object = hashlib.sha384()
            elif algorithm == 'sha512':
                hash_object = hashlib.sha512()
            elif algorithm == 'md5':
                hash_object = hashlib.md5()
            else:
                raise ValueError("Invalid hashing algorithm. Supported algorithms: 'sha1', 'sha256', 'sha384', 'sha512', 'md5'")
            with open(file, "rb") as f:
                while True:
                    data = f.read(65536)
                    if not data:
                        break
                    hash_object.update(data)
            return (hash_object.hexdigest()).upper() if as_upper else (hash_object.hexdigest()).lower()
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")