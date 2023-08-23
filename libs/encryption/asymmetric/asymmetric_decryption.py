from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

def TELADecrypt(ciphertext: str, private_key: rsa.RSAPrivateKey) -> str:
        """
        Decrypts the given ciphertext using a private key.
        """
        plaintext = private_key.decrypt(
            bytes.fromhex(ciphertext),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA512()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        return plaintext.decode()