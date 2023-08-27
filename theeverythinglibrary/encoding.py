import base64

class TELEncoding():
    '''
    WIP! Coming soon
    '''
    def __init__(self) -> None:
        pass

    def base64_encode(self, plaintext: str, encoding: str = 'utf-8') -> str:
        '''
        WIP! Coming soon
        '''
        try:
            encoded_bytes = base64.b64encode(plaintext.encode(encoding=encoding))
            encoded_string = encoded_bytes.decode(encoding=encoding)
            return encoded_string
        except UnicodeEncodeError as msg:
            raise UnicodeEncodeError(f"There was an error when encoding the text: {msg}")
        except UnicodeDecodeError as msg:
            raise UnicodeDecodeError(f"There was an error when decoding the text: {msg}")
        except Exception as msg:
            raise Exception(f"There was an error when encoding the text: {msg}")
    
    def base64_decode(self, plaintext: str, encoding: str) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            decoded_bytes = base64.b64decode(plaintext.encode(encoding=encoding))
            decoded_string = decoded_bytes.decode(encoding=encoding)
            return decoded_string
        except UnicodeEncodeError as msg:
            raise UnicodeEncodeError(f"There was an error when encoding the text: {msg}")
        except UnicodeDecodeError as msg:
            raise UnicodeDecodeError(f"There was an error when decoding the text: {msg}")
        except Exception as msg:
            raise Exception(f"There was an error when encoding the text: {msg}")

    def hex_encode(self, plaintext: str, encoding: str = 'utf-8') -> str:
        '''
        WIP! Coming soon
        '''
        try:
            encoded_string = plaintext.encode(encoding=encoding).hex()
            return encoded_string
        except UnicodeEncodeError as msg:
            raise UnicodeEncodeError(f"There was an error when encoding the text: {msg}")
        except UnicodeDecodeError as msg:
            raise UnicodeDecodeError(f"There was an error when decoding the text: {msg}")
        except Exception as msg:
            raise Exception(f"There was an error when encoding the text: {msg}")
    
    def hex_decode(self, encoded_text: str, encoding: str = 'utf-8') -> str:
        '''
        WIP! Coming soon
        '''
        try:
            decoded_string = bytes.fromhex(encoded_text).decode(encoding=encoding)
            return decoded_string
        except UnicodeEncodeError as msg:
            raise UnicodeEncodeError(f"There was an error when encoding the text: {msg}")
        except UnicodeDecodeError as msg:
            raise UnicodeDecodeError(f"There was an error when decoding the text: {msg}")
        except Exception as msg:
            raise Exception(f"There was an error when encoding the text: {msg}")
        
    def binary_encode(self, plaintext: str, as_bytes: bool = False) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            if as_bytes:
                encoded_bytes = bytes([ord(char) for char in plaintext])
            else:
                encoded_bytes = ' '.join(format(ord(char), '08b') for char in plaintext)
            return encoded_bytes
        except UnicodeEncodeError as msg:
            raise UnicodeEncodeError(f"There was an error when encoding the text: {msg}")
        except UnicodeDecodeError as msg:
            raise UnicodeDecodeError(f"There was an error when decoding the text: {msg}")
        except Exception as msg:
            raise Exception(f"There was an error when encoding the text: {msg}")
    
    def binary_decode(self, encoded_text: str | bytes) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            if type(encoded_text) == str:
                binary_list = encoded_text.split()
                decoded_string = ''.join(chr(int(binary, 2)) for binary in binary_list)
            elif type(encoded_text) == bytes:
                decoded_string = ''.join(chr(byte) for byte in encoded_text)
            return decoded_string
        except UnicodeEncodeError as msg:
            raise UnicodeEncodeError(f"There was an error when encoding the text: {msg}")
        except UnicodeDecodeError as msg:
            raise UnicodeDecodeError(f"There was an error when decoding the text: {msg}")
        except Exception as msg:
            raise Exception(f"There was an error when encoding the text: {msg}")
