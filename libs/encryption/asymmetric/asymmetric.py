from libs.encryption.asymmetric.asymmetric_encryption import TELAEncrypt

from cryptography.hazmat.primitives.asymmetric import rsa

class TELAsymmetric():
    '''
    This is the main class for the symmetric encryption and deryption

    Arguments:
     - No agruments
    '''

    def __init__(self) -> None:
        pass

    def generate_key_pair(self):
        pass

    def encrypt(self, plaintext: str, public_key: rsa.RSAPublicKey, return_as_string: bool):
        '''
        
        '''
        try:
            TELAEncrypt(plaintext=plaintext, public_key=public_key, return_string=return_as_string)
        except Exception as msg:
            print(f"There was an error when encryption the text!\n{msg}")
            return "ERROR"