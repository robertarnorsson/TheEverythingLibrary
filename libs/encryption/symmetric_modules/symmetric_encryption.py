import base64
import os
import uuid
from cryptography.fernet import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def MS_Encrypt(iteration: int, plaintext: str, password: str, salt_length: int = 32, key_length: int = 32):
    """Encrypts a string using a password"""

    plaintext = plaintext.encode()
    password = password.encode()

    salt = os.urandom(salt_length)

    # Generate a key using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA384(),
        salt=salt,
        iterations=iteration,  # Use a larger iteration count for increased security
        length=key_length,
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