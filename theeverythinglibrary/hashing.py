import os
import argon2
import hashlib

class TELHash:
    '''
    ## Hash
    ---
    This class provides utility functions for generating salt and pepper, hash passwords, and hash verification.

    **Note:** This class uses the Argon2 password hashing algorithm for secure password storage.
    '''

    def __init__(self):
        pass

    def generate_salt(self, salt_len: int = 16) -> str:
        '''
        ## Generate salt
        ---
        Generates a random salt for password hashing.\n
        ---
        ### Arguments:
            - `salt_len` (optional): The length of the generated salt in bytes (default is `16`).\n
        ---
        ### Returns:
            - The randomly generated salt in hexadecimal format.\n
        '''
        try:
            salt = os.urandom(salt_len).hex()
            return salt
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def generate_pepper(self, pepper_len: int = 16) -> str:
        '''
        ## Generate pepper
        ---
        Generates a random pepper for password hashing.\n
        ---
        ### Arguments:
            - `pepper_len` (optional): The length of the generated pepper in bytes (default is `16`).\n
        ---
        ### Returns:
            - The randomly generated pepper in hexadecimal format.\n
        '''
        try:
            pepper = os.urandom(pepper_len).hex()
            return pepper
        except Exception as e:
                raise Exception(f"Something went wrong: {e}")

    def hash(self, password: str, salt: str, pepper: str) -> str:
        '''
        ## Hash password
        ---
        Hashes a password using Argon2 with a given salt and pepper.
        ---
        ### Arguments:
            - `password`: The password to be hashed.
            - `salt`: The salt used for password hashing.
            - `pepper`: The pepper used for password hashing.
        ---
        ### Returns:
            - The hashed password.
        ---
        ### Note:
        The generated hash is encoded in ASCII and can be securely stored.
        '''
        try:
            password += salt
            password += pepper

            hasher = argon2.PasswordHasher(
                hash_len=80,
                salt_len=32,
                time_cost=10,
                memory_cost=2**12,
                parallelism=6,
                encoding='ascii'
            )
            hashed_password = hasher.hash(password)
            return hashed_password
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def verify(self, hashed_password: str, password: str, salt: str, pepper: str, raise_error: bool = False) -> bool:
        '''
        ## Verify hash
        ---
        Verifies a password against its hashed version using Argon2 with the provided salt and pepper.\n
        ---
        ### Arguments:
            - `hashed_password`: The previously hashed password.\n
            - `password`: The password to be verified.\n
            - `salt`: The salt used for password hashing.\n
            - `pepper`: The pepper used for password hashing.\n
            - `raise_error` (optional): Should the function raise an error if the hashes does not match (default is `False`).\n
        ---
        ### Returns:
            - True if the password is valid, False otherwise (if `raise_error` is false).\n
        ---
        ### Exceptions
            - If verification failed, the hash is invalid or an error occurs during verification.\n
        '''
        try:
            salt = str(salt)
            pepper = str(pepper)

            password += salt
            password += pepper

            hasher = argon2.PasswordHasher(
                hash_len=80,
                salt_len=32,
                time_cost=10,
                memory_cost=2**12,
                parallelism=6,
                encoding='ascii'
            )

            hasher.verify(hashed_password, password)
            return True
        except argon2.exceptions.VerificationError:
            if not raise_error:
                return False
            else:
                raise argon2.exceptions.VerificationError(f"Verification Failed: {e}")
        except argon2.exceptions.InvalidHash:
            if not raise_error:
                return False
            else:
                raise argon2.exceptions.InvalidHash(f"The hash is an invalid hash: {e}")
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def hash_file(self, file_path: str, algorithm: str = 'sha256', as_upper: bool = True) -> str:
        '''
        ## Hash File
        ---
        Calculates the hash of a file for integrity checks using a specified algorithm (default is `SHA-256`).
        ---
        ### Arguments:
            - `file_path`: The path to the file to be hashed.
            - `algorithm` (optional): The hashing algorithm to use (default is `sha256`). Supported algorithms: `sha1`, `sha256`, `sha384`, `sha512`, `md5`.
            - `as_upper` (optional): Should return hash in upper case (default is `True`).
        ---
        ### Returns:
            - The hash of the file in hexadecimal format.
        ---
        ### Exceptions:
            - If an error occurs during file reading or hashing or an error occurs something else.
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
            with open(file_path, "rb") as file:
                while True:
                    data = file.read(65536)
                    if not data:
                        break
                    hash_object.update(data)
            return (hash_object.hexdigest()).upper() if as_upper else hash_object.hexdigest()
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")