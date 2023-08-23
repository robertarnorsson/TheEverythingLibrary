import base64
from cryptography.exceptions import InvalidTag
from cryptography.fernet import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def TELSDecrypt(iteration: int, ciphertext: str, password: str, salt_length: int = 32, key_length: int = 32):
    """Decrypts a string using a password and salt."""

    password = password.encode()

    # Decode the base64-encoded ciphertext
    ciphertext = base64.urlsafe_b64decode(ciphertext)

    # Extract the salt, nonce, and tag
    salt = ciphertext[:salt_length]
    nonce = ciphertext[salt_length:salt_length+64]
    tag = ciphertext[salt_length+64:salt_length+64+16]
    ciphertext = ciphertext[salt_length+64+16:]

    # Generate the same key using PBKDF2HMAC
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA384(),
        salt=salt,
        iterations=iteration,
        length=key_length,
        backend=default_backend()
    )
    key = kdf.derive(password)

    # Use AES-GCM for authenticated decryption
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
    decryptor = cipher.decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext.decode()