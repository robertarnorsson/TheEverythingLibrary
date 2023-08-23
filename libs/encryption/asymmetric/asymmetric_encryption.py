from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

def TELAEncrypt(plaintext: str, public_key: rsa.RSAPublicKey, return_string: bool=False) -> bytes | str | None:
        """Encrypts the given text using a public key."""
        ciphertext = public_key.encrypt(
            plaintext.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA512()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        if return_string:
            return ciphertext.hex()
        else:
            return ciphertext