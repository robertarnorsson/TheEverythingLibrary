from everything.encryption.symmetric_modules.symmetric_encryption import MS_Encrypt
from everything.encryption.symmetric_modules.symmetric_decryption import MS_Decrypt

from cryptography.exceptions import InvalidTag

class TELSymmetric():
    '''
    This is the main class for the symmetric encryption and deryption

    Arguments:
     - Iterations refer to the process of repeatedly applying a cryptographic algorithm a certain number of times to enhance security and complexity (Minimum: 100000)
     - Salt length determines the size of the random data added to plaintext before hashing or encrypting in password storage, enhancing security by preventing rainbow table attacks
     - The key length in encryption determines the size of the cryptographic key, directly influencing the security and strength of the encryption algorithm
    '''
    def __init__(self, iterations: int = 100000, salt_length: int = 32, key_length: int = 32) -> None:

        # Set iterations to minimum of 100000
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
        Encrypt the given text using a password to generate a key

        Arguments:
         - Plaintext is the text that is being encrypted
         - Password is the text that the encrpytion key is generated from

        Return:
         - Returns the encrypted text if no error occured

        Exeptions:
         - (ERROR) The standard error that is raised when something goes wrong
        '''
        try:
            return MS_Encrypt(iteration=self.iterations, plaintext=plaintext, password=password, salt_length=self.salt_length)
        except Exception as msg:
            print(f"There was an error when encryption the text!\n{msg}")
            return "ERROR"
        
    def decrypt(self, ciphertext: str, password: str) -> str:
        '''
        Encrypt the given text using a password to generate a key

        Arguments:
         - Ciphertext is the text that has been encrypted
         - Password is the text that the encrpytion key is generated from

        Return:
         - Returns the decrypted text if no error occured and the password is correct

        Exeptions:
         - (InvalidTag) This error is raised when the password is wrong or the ciphertext has been tampered with
         - (ERROR) The standard error that is raised when something goes wrong
        '''
        try:
            return MS_Decrypt(iteration=self.iterations, ciphertext=ciphertext, password=password, salt_length=self.salt_length)
        except InvalidTag:
            print("The password was wrong or the cipertext has been tampered with")
            return "InvalidTag"
        except Exception as msg:
            print(f"There was an error when encryption the text!\n{msg}")
            return "ERROR"