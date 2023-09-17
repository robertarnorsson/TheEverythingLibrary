from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidTag

import os
import base64
import uuid
from typing import Tuple

class TELSymmetric:
    '''
    ## Symmetric Encryption
    ---
    This class provides utility functions for encrypting and decrypting text.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self, iterations: int = 100000, salt_length: int = 32, key_length: int = 32) -> None:
        '''
        ## Constructor
        ---
        ### Description
        Initialize the TELSymmetric encryption utility.\n
        ---
        ### Arguments
            - `iterations` (optional): The number of PBKDF2 iterations (default is 100000).
            - `salt_length` (optional): The length of the salt in bytes (default is 32).
            - `key_length` (optional): The length of the encryption key in bytes (default is 32).\n
        '''
        if iterations < 100000:
            self.iterations = 100000
        else:
            self.iterations = iterations
        
        if salt_length < 16:
            self.salt_length = 16
        else:
            self.salt_length = salt_length

        if key_length < 32:
            self.key_length = 32
        else:
            self.key_length = key_length

    def encrypt(self, plaintext: str, password: str) -> str:
        '''
        ## Encrypt
        ---
        ### Description
        Encrypt a plaintext message using symmetric encryption.\n
        ---
        ### Arguments
            - `plaintext`: The text to be encrypted.
            - `password`: The password used for encryption.\n
        ---
        ### Return
            - The encrypted ciphertext.\n
        ---
        ### Exceptions
            - If an error occurs during encryption.\n
        '''
        try:
            plaintext = plaintext.encode()
            password = password.encode()

            salt = os.urandom(self.salt_length)

            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA384(),
                salt=salt,
                iterations=self.iterations,
                length=self.key_length,
                backend=default_backend()
            )
            key = kdf.derive(password)

            nonce = os.urandom(32) + uuid.uuid4().bytes + uuid.uuid4().bytes
            
            cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(plaintext) + encryptor.finalize()

            ciphertext_with_nonce_tag = encryptor.tag + ciphertext

            return base64.urlsafe_b64encode(salt + nonce + ciphertext_with_nonce_tag).decode()
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
        
    def decrypt(self, ciphertext: str, password: str) -> str:
        '''
        ## Decrypt
        ---
        ### Description
        Decrypt an encrypted ciphertext using symmetric decryption.\n
        ---
        ### Arguments
            - `ciphertext`: The ciphertext to be decrypted.
            - `password`: The password used for decryption.\n
        ---
        ### Return
            - The decrypted plaintext.\n
        ---
        ### Exceptions
            - If the password is wrong, the ciphertext has been tampered with, or an error occurs during decryption.\n
        '''
        try:
            password = password.encode()

            # Decode the base64-encoded ciphertext
            ciphertext = base64.urlsafe_b64decode(ciphertext)

            # Extract the salt, nonce, and tag
            salt = ciphertext[:self.salt_length]
            nonce = ciphertext[self.salt_length:self.salt_length+64]
            tag = ciphertext[self.salt_length+64:self.salt_length+64+16]
            ciphertext = ciphertext[self.salt_length+64+16:]

            # Generate the same key using PBKDF2HMAC
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA384(),
                salt=salt,
                iterations=self.iterations,
                length=self.key_length,
                backend=default_backend()
            )
            key = kdf.derive(password)

            # Use AES-GCM for authenticated decryption
            cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
            decryptor = cipher.decryptor()

            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            return plaintext.decode()
        except InvalidTag:
            raise InvalidTag("The password was wrong or the ciphertext has been tampered with")
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

class TELAsymmetric:
    '''
    ## Asymmetric Encryption
    ---
    This class provides utility functions for managing asymmetrical keys, encryption and decryption.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_key_pair() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        '''
        ## Generate Key Pair
        ---
        ### Description
        Generate a pair of RSA private and public keys.\n
        ---
        ### Return
            - A tuple containing the generated private and public keys.\n
        ---
        ### Exceptions
            - If an error occurs during key generation.\n
        '''
        try:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            public_key = private_key.public_key()
            return (private_key, public_key)
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    @staticmethod
    def encrypt(plaintext: str, public_key: rsa.RSAPublicKey) -> str:
        '''
        ## Encrypt
        ---
        ### Description
        Encrypt a plaintext using the provided RSA public key.\n
        ---
        ### Arguments
            - `plaintext`: The text to be encrypted.
            - `public_key`: The RSA public key used for encryption.\n
        ---
        ### Return
            - The encrypted ciphertext in hexadecimal format.\n
        ---
        ### Exceptions
            - If an error occurs during encryption.\n
        '''
        try:
            ciphertext = public_key.encrypt(
                plaintext.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA512()),
                    algorithm=hashes.SHA512(),
                    label=None
                )
            )
            return ciphertext.hex()
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    @staticmethod
    def decrypt(ciphertext: str, private_key: rsa.RSAPrivateKey) -> str:
        '''
        ## Decrypt
        ---
        ### Description
        Decrypt an RSA-encrypted ciphertext.\n
        ---
        ### Arguments
            - `ciphertext`: The encrypted ciphertext in hexadecimal format.
            - `private_key`: The RSA private key used for decryption.\n
        ---
        ### Return
            - The decrypted plaintext.\n
        ---
        ### Exceptions
            - If the ciphertext or key is invalid, or if an error occurs during decryption.\n
        '''
        try:
            plaintext = private_key.decrypt(
                bytes.fromhex(ciphertext),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA512()),
                    algorithm=hashes.SHA512(),
                    label=None
                )
            )
            return plaintext.decode()
        except ValueError as e:
            raise ValueError(f"The ciphertext or key is wrong or not matching\n{e}")
        except TypeError as e:
            raise TypeError(f"The ciphertext or key is wrong or not matching\n{e}")
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")
    
    @staticmethod
    def store_private_key(private_key: rsa.RSAPrivateKey, password: str, path: str, file_name: str = "private_key") -> None:
        '''
        ## Store Private Key
        ---
        ### Description
        Store the RSA private key securely in a file using password-based encryption.\n
        ---
        ### Arguments
            - `private_key`: The RSA private key to be stored.
            - `password`: The password used for encryption.
            - `path`: The directory path where the key file will be stored.
            - `file_name` (optional): The name of the key file (default is "private_key").\n
        ---
        ### Exceptions
            - If an error occurs during key storage.\n
        '''
        try:
            pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.BestAvailableEncryption(password=password.encode())
            )
            b64_pem = base64.a85encode(pem, foldspaces=False, wrapcol=64, pad=True)
            with open(os.path.join(path, f'{file_name}.pem'), 'wb') as f:
                f.write(b64_pem)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error storing private key: {e}")
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")
    
    @staticmethod
    def store_public_key(public_key: rsa.RSAPrivateKey, path: str, file_name: str = "public_key") -> None:
        '''
        ## Store Public Key
        ---
        ### Description
        Store the RSA public key in a file.\n
        ---
        ### Arguments
            - `public_key`: The RSA public key to be stored.
            - `path`: The directory path where the key file will be stored.
            - `file_name` (optional): The name of the key file (default is "public_key").\n
        ---
        ### Exceptions
            - If an error occurs during key storage.\n
        '''
        try:
            pem = public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            b64_pem = base64.a85encode(pem, foldspaces=False, wrapcol=64, pad=True)
            with open(os.path.join(path, f'{file_name}.pem'), 'wb') as f:
                f.write(b64_pem)
        except FileNotFoundError as msg:
            raise FileNotFoundError(f"Error storing public key: {msg}")
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")
    
    @staticmethod
    def get_private_key(password: str, path: str, file_name: str = "private_key") -> rsa.RSAPrivateKey:
        '''
        ## Get Private Key
        ---
        ### Description
        Retrieve the stored RSA private key from a file.\n
        ---
        ### Arguments
            - `password`: The password used for decryption.
            - `path`: The directory path where the key file is stored.
            - `file_name` (optional): The name of the key file (default is "private_key").\n
        ---
        ### Return
            - The retrieved RSA private key.\n
        ---
        ### Exceptions
            - If the file is not found, the password is wrong, or an error occurs during key retrieval.\n
        '''
        try:
            with open(os.path.join(path, f'{file_name}.pem'), "rb") as f:
                key = base64.a85decode(f.read())
                private_key = serialization.load_pem_private_key(
                    key,
                    password=password.encode(),
                    backend=default_backend()
                )
            if private_key:
                return private_key
            else:
                raise Exception
        except FileNotFoundError as msg:
            raise FileNotFoundError(f"Error looking for private key: {msg}")
        except ValueError as msg:
            raise ValueError(f"The password is wrong: {msg}")
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")
    
    @staticmethod
    def get_public_key(path: str, file_name: str = "public_key") -> rsa.RSAPublicKey:
        '''
        ## Get Public Key
        ---
        ### Description
        Retrieve the stored RSA public key from a file.\n
        ---
        ### Arguments
            - `path`: The directory path where the key file is stored.
            - `file_name` (optional): The name of the key file (default is "public_key").\n
        ---
        ### Return
            - The retrieved RSA public key.\n
        ---
        ### Exceptions
            - If the file is not found or an error occurs during key retrieval.\n
        '''
        try:
            with open(os.path.join(path, f'{file_name}.pem'), "rb") as f:
                key = base64.a85decode(f.read())
                public_key = serialization.load_pem_public_key(
                    key,
                    backend=default_backend()
                )
            if public_key:
                return public_key
            else:
                raise Exception
        except FileNotFoundError as msg:
            raise FileNotFoundError(f"Error looking for public key: {msg}")
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")