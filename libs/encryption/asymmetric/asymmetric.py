from libs.encryption.asymmetric.asymmetric_encryption import TELAEncrypt
from libs.encryption.asymmetric.asymmetric_decryption import TELADecrypt
from libs.encryption.asymmetric.asymmetric_key import TELAGenerateKeys
from libs.encryption.asymmetric.asymmetric_key_storage import TELAStorePrivateKey
from libs.encryption.asymmetric.asymmetric_key_storage import TELAStorePublicKey
from libs.encryption.asymmetric.asymmetric_key_storage import TELAGetPrivateKey
from libs.encryption.asymmetric.asymmetric_key_storage import TELAGetPublicKey

from cryptography.hazmat.primitives.asymmetric import rsa

class TELAsymmetric():
    '''
    This is the main class for the asymmetric encryption and deryption pluss key management

    Arguments:
     - No arguments
    '''

    def __init__(self) -> None:
        pass

    def generate_key_pair(self):
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
            return TELAGenerateKeys()
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
            return TELAEncrypt(plaintext=plaintext, public_key=public_key)
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
         - (ERROR) The standard error that is raised when something goes wrong
        '''
        try:
            return TELADecrypt(ciphertext=ciphertext, private_key=private_key)
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
            TELAStorePrivateKey(private_key=private_key, password=password, path=path, file_name=file_name)
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
            TELAStorePublicKey(public_key=public_key, path=path, file_name=file_name)
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
            key = TELAGetPrivateKey(password=password, path=path, file_name=file_name)
            if key:
                return key
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
            key = TELAGetPublicKey(path=path, file_name=file_name)
            if key:
                return key
            else:
                raise Exception
        except FileNotFoundError as msg:
            print(f"The file that you want to access was not found\n{msg}")
        except Exception as msg:
            print(f"There was an error when storing the keys!\n{msg}")