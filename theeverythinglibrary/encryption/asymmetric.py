from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

import os
import base64
from typing import Tuple

class TELAsymmetric():
    '''
    This is the main class for the asymmetric encryption and deryption pluss key management

    Arguments:
     - No arguments
    '''

    def __init__(self) -> None:
        pass

    def generate_key_pair(self) -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        '''
        Generates a key pair, one public key used for encrypting and a private key used for decryption

        Arguments:
         - No arguments

        Return:
         - Returns the key pair as Private key then Public key

        Exeptions:
         - (ERROR) The standard error that is raised when something goes wrong
        '''
        try:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            public_key = private_key.public_key()
            return (private_key, public_key)
        except Exception as msg:
            print(f"There was an error when generating the keys!\n{msg}")
            return "ERROR"

    def encrypt(self, plaintext: str, public_key: rsa.RSAPublicKey) -> str:
        '''
        Encrypt the given text using a given public key

        Arguments:
         - Plaintext is the text that is being encrypted
         - Public key used for encryption

        Return:
         - Returns the encrypted text if no error occured

        Exeptions:
         - (ERROR) The standard error that is raised when something goes wrong
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
        except Exception as msg:
            print(f"There was an error when encryption the text!\n{msg}")
            return "ERROR"

    def decrypt(self, ciphertext: str, private_key: rsa.RSAPrivateKey) -> str:
        '''
        Encrypt the given text using a password to generate a key

        Arguments:
         - Ciphertext is the text that has been encrypted
         - Private key used for the decryption of the ciphertext

        Return:
         - Returns the decrypted text if no error occured and the private key is correct

        Exeptions:
         - (ValueError) The given private key is wrong or the ciphertext has been tamperd with
         - (TypeError) The given private key is wrong or the ciphertext has been tamperd with
         - (ERROR) The standard error that is raised when something goes wrong
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
        except ValueError as msg:
            print(f"The ciphertext or key is wrong or not matching\n{msg}")
            return "ValueError"
        except TypeError as msg:
            print(f"The ciphertext or key is wrong or not matching\n{msg}")
            return "ValueError"
        except Exception as msg:
            print(f"There was an error when decrypting the text!\n{msg}")
            return "ERROR"
    
    def store_private_key(self, private_key: rsa.RSAPrivateKey, password: str, path: str, file_name: str = "private_key") -> None:
        '''
        Store the private key in a file encrypted and encoded with a password and Ascii85

        Arguments
         - Private key is the key that is stored
         - Password is the password used to encrypt and decrypt the private key
         - Path is the path to where the key are stored
         - File name is the name that the file with the key has

        Return:
         - No returns

        Exeptions:
         - (FileNotFoundError) The path or file name is wrong
         - (ERROR) The standard error that is raised when something goes wrong
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
        except FileNotFoundError as msg:
            print(f"The file that you want to access was not found or something went wrong when trying to create a new file\n{msg}")
        except Exception as msg:
            print(f"There was an error when storing the keys!\n{msg}")
    
    def store_public_key(self, public_key: rsa.RSAPrivateKey, path: str, file_name: str = "public_key") -> None:
        '''
        Store the public key in a file encoded in Ascii85

        Arguments:
         - Public key used for the encryption of the plaintext
         - Path is the path to where the key are stored
         - File name is the name that the file with the key has

        Return:
         - No returns

        Exeptions:
         - (FileNotFoundError) The path or file name is wrong
         - (ERROR) The standard error that is raised when something goes wrong
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
            print(f"The file that you want to access was not found or something went wrong when trying to create a new file\n{msg}")
        except Exception as msg:
            print(f"There was an error when storing the keys!\n{msg}")
    
    def get_private_key(self, password: str, path: str, file_name: str = "private_key") -> rsa.RSAPrivateKey:
        '''
        Retrives a private key from a file and decrypts it using a password

        Arguments:
         - Password is the password used to encrypt and decrypt the private key
         - Path is the path to where the key are stored
         - File name is the name that the file with the key has

        Return:
         - No returns

        Exeptions:
         - (FileNotFoundError) The path or file name is wrong
         - (ValueError) The given password is incorrect
         - (ERROR) The standard error that is raised when something goes wrong
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
            print(f"The file that you want to access was not found\n{msg}")
        except ValueError as msg:
            print(f"The password is wrong!\n{msg}")
        except Exception as msg:
            print(f"There was an error when storing the keys!\n{msg}")
    
    def get_public_key(self, path: str, file_name: str = "public_key") -> rsa.RSAPublicKey:
        '''
        Retrives a private key from a file and decrypts it using a password

        Arguments:
         - Password is the password used to encrypt and decrypt the private key
         - Path is the path to where the key are stored
         - File name is the name that the file with the key has

        Return:
         - No returns

        Exeptions:
         - (FileNotFoundError) The path or file name is wrong
         - (ERROR) The standard error that is raised when something goes wrong
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
            print(f"The file that you want to access was not found\n{msg}")
        except Exception as msg:
            print(f"There was an error when storing the keys!\n{msg}")