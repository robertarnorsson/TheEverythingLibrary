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

    def generate_salt(self, length: int = 16) -> str:
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

    def hash(self, password: str, salt: str, pepper: str | None = None, encode_hash: bool = True, params: dict | None = None) -> str:
        '''
        ## Hash password
        ---
        Hashes a password using Argon2 with a given salt and pepper.\n
        ---
        ### Arguments:
            - `password`: The password to be hashed.\n
            - `salt`: The salt used for password hashing.\n
            - `pepper` (optional): The pepper used for password hashing (default is `None`).\n
            - `params` (optional): Additional parameters for the hashing function (default is `None`).\n
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
            password if pepper == None else f"{password}{pepper}"

            default_params = {
                "hash_len": 80,
                "salt_len": len(salt),
                "time_cost": 10,
                "memory_cost": 2**12,
                "parallelism": 6,
                "encoding": 'ascii'
            }

            if params != None and params != {}:
                default_params.update(params)

            hasher = argon2.PasswordHasher(
                hash_len=default_params["hash_len"],
                salt_len=default_params["salt_len"],
                time_cost=default_params["time_cost"],
                memory_cost=default_params["memory_cost"],
                parallelism=default_params["parallelism"],
                encoding=default_params["encoding"]
            )
            hashed_password = hasher.hash(password)
            return hashed_password if not encode_hash else base64.urlsafe_b64encode(base64.a85encode(hashed_password.encode())).decode()
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
        Calculates the hash of a file for integrity checks using a specified algorithm (default is `SHA-256`).\n
        ---
        ### Arguments:
            - `file_path`: The path to the file to be hashed.\n
            - `algorithm` (optional): The hashing algorithm to use (default is `sha256`). Supported algorithms: `sha1`, `sha256`, `sha384`, `sha512`, `md5`.\n
            - `as_upper` (optional): Should return hash in upper case (default is `True`).\n
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
            with open(file_path, "rb") as file:
                while True:
                    data = file.read(65536)
                    if not data:
                        break
                    hash_object.update(data)
            return (hash_object.hexdigest()).upper() if as_upper else (hash_object.hexdigest()).lower()
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
        

tel_hash = TELHash()

text1 = "Passw0rd"
text2 = "Passw0rdLooonger123"
text3 = "Passw0rdSUUUUPPPERRRRLOOOOOONNNG!!!"
text4 = "Passw0rdSUUUUPPPERRRRLOOOOOONNNG!!!-----------------SUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUPPPPPPPPPPPPPPPPPPPEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRLLLLLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------SuperLong"

salt = tel_hash.generate_salt(length=32)

hashed_password1 = tel_hash.hash(text1, salt=salt, params={"hash_len": 12})
hashed_password2 = tel_hash.hash(text2, salt=salt, encode_hash=False, params={"hash_len": 10})
hashed_password3 = tel_hash.hash(text3, salt=salt)
hashed_password4 = tel_hash.hash(text4, salt=salt)

print(hashed_password1)
print(hashed_password2)
print(hashed_password3)
print(hashed_password4)