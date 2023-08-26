from cryptography.fernet import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidTag

import base64
import os
import uuid

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
            plaintext = plaintext.encode()
            password = password.encode()

            salt = os.urandom(self.salt_length)

            # Generate a key using PBKDF2HMAC
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA384(),
                salt=salt,
                iterations=self.iterations,  # Use a larger iteration count for increased security
                length=self.key_length,
                backend=default_backend()
            )
            key = kdf.derive(password)

            # Generate a random nonce
            nonce = os.urandom(32) + uuid.uuid4().bytes + uuid.uuid4().bytes
            
            # Use AES-GCM for authenticated encryption
            cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(plaintext) + encryptor.finalize()

            # Serialize the nonce and tag with the ciphertext
            ciphertext_with_nonce_tag = encryptor.tag + ciphertext

            return base64.urlsafe_b64encode(salt + nonce + ciphertext_with_nonce_tag).decode()
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
            print("The password was wrong or the cipertext has been tampered with")
            return "InvalidTag"
        except Exception as msg:
            print(f"There was an error when encryption the text!\n{msg}")
            return "ERROR"