from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

from typing import Tuple

def TELAGenerateKeys() -> Tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
    """
    Generates a private and a public key for the user and returns a tuple.

    Return: (PrivateKey, PublicKey)
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return (private_key, public_key)