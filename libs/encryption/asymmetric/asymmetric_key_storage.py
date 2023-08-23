from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

import os
import base64

def TELAStorePrivateKey(private_key: rsa.RSAPrivateKey, password: str, path: str, file_name: str) -> None:
    """
    Stores the private key for the user at a specefied path.
    The key is stored encrypted using a password provided by the user and base64 encoded.

    Return: Does not return
    """

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password=password.encode())
    )
    b64_pem = base64.a85encode(pem, foldspaces=False, wrapcol=64, pad=True)
    with open(os.path.join(path, f'{file_name}.pem'), 'wb') as f:
        f.write(b64_pem)

def TELAStorePublicKey(public_key: rsa.RSAPublicKey, path: str, file_name: str) -> None:
    """
    Stores the public key for the user at a specefied path.
    The key is stored base64 encoded.

    Return: Does not return
    """

    pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    b64_pem = base64.a85encode(pem, foldspaces=False, wrapcol=64, pad=True)
    with open(os.path.join(path, f'{file_name}.pem'), 'wb') as f:
        f.write(b64_pem)

def TELAGetPrivateKey(password: str, path: str, file_name: str) -> rsa.RSAPrivateKey:
    """
    Gets the private key and loads it using the provided password and then returns it.

    Return: PrivateKey
    """
    with open(os.path.join(path, f'{file_name}.pem'), "rb") as f:
        key = base64.a85decode(f.read())
        private_key = serialization.load_pem_private_key(
            key,
            password=password.encode(),
            backend=default_backend()
        )
        return private_key

def TELAGetPublicKey(path: str, file_name: str) -> rsa.RSAPublicKey:
    """
    Gets the public key and loads it and then returns it.

    Return: PublicKey
    """
    with open(os.path.join(path, f'{file_name}.pem'), "rb") as f:
        key = base64.a85decode(f.read())
        public_key = serialization.load_pem_public_key(
            key,
            backend=default_backend()
        )
        return public_key