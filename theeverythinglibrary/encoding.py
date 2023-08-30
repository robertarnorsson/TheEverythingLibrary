import base64

class TELEncoding:
    '''
    ## Encoding & Decoding
    ---
    This class provides utility functions for encoding and decoding in different formats.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self) -> None:
        pass

    def base64_encode(self, plaintext: str, encoding: str = 'utf-8') -> str:
        '''
        ## Base64 Encode
        ---
        ### Description
        Encode the given plaintext using Base64 encoding.\n
        ---
        ### Arguments
            - `plaintext`: The text to encode.
            - `encoding` (optional): The character encoding to use (default is 'utf-8').\n
        ---
        ### Return
            - The Base64 encoded string.\n
        ---
        ### Exceptions
            - If an error occurs during encoding.\n
        '''
        try:
            encoded_bytes = base64.b64encode(plaintext.encode(encoding=encoding))
            encoded_string = encoded_bytes.decode(encoding=encoding)
            return encoded_string
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def base64_decode(self, encoded_text: str, encoding: str = 'utf-8') -> str:
        '''
        ## Base64 Decode
        ---
        ### Description
        Decode a Base64 encoded string.\n
        ---
        ### Arguments
            - `encoded_text`: The Base64 encoded string to decode.
            - `encoding` (optional): The character encoding to use (default is 'utf-8').\n
        ---
        ### Return
            - The decoded string.\n
        ---
        ### Exceptions
            - If an error occurs during decoding.\n
        '''
        try:
            decoded_bytes = base64.b64decode(encoded_text.encode(encoding=encoding))
            decoded_string = decoded_bytes.decode(encoding=encoding)
            return decoded_string
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def hex_encode(self, plaintext: str, encoding: str = 'utf-8') -> str:
        '''
        ## Hexadecimal Encode
        ---
        ### Description
        Encode the given plaintext into a hexadecimal string.\n
        ---
        ### Arguments
            - `plaintext`: The text to encode.
            - `encoding` (optional): The character encoding to use (default is 'utf-8').\n
        ---
        ### Return
            - The hexadecimal encoded string.\n
        ---
        ### Exceptions
            - If an error occurs during encoding.\n
        '''
        try:
            encoded_string = plaintext.encode(encoding=encoding).hex()
            return encoded_string
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def hex_decode(self, encoded_text: str, encoding: str = 'utf-8') -> str:
        '''
        ## Hexadecimal Decode
        ---
        ### Description
        Decode a hexadecimal encoded string.\n
        ---
        ### Arguments
            - `encoded_text`: The hexadecimal encoded string to decode.
            - `encoding` (optional): The character encoding to use (default is 'utf-8').\n
        ---
        ### Return
            - The decoded string.\n
        ---
        ### Exceptions
            - If an error occurs during decoding.\n
        '''
        try:
            decoded_string = bytes.fromhex(encoded_text).decode(encoding=encoding)
            return decoded_string
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def binary_encode(self, plaintext: str, as_bytes: bool = False) -> str | bytes:
        '''
        ## Binary Encode
        ---
        ### Description
        Encode the given plaintext into binary representation.\n
        ---
        ### Arguments
            - `plaintext`: The text to encode.
            - `as_bytes` (optional): If `True`, return the encoded result as bytes (default is `False`).\n
        ---
        ### Return
            - The binary encoded result as a string or bytes.\n
        ---
        ### Exceptions
            - If an error occurs during encoding.\n
        '''
        try:
            if as_bytes:
                encoded_bytes = bytes([ord(char) for char in plaintext])
            else:
                encoded_bytes = ' '.join(format(ord(char), '08b') for char in plaintext)
            return encoded_bytes
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def binary_decode(self, encoded_text: str | bytes) -> str:
        '''
        ## Binary Decode
        ---
        ### Description
        Decode binary encoded data into a string.\n
        ---
        ### Arguments
            - `encoded_text`: The binary encoded data to decode.\n
        ---
        ### Return
            - The decoded string.\n
        ---
        ### Exceptions
            - If an error occurs during decoding.\n
        '''
        try:
            if type(encoded_text) == str:
                binary_list = encoded_text.split()
                decoded_string = ''.join(chr(int(binary, 2)) for binary in binary_list)
            elif type(encoded_text) == bytes:
                decoded_string = ''.join(chr(byte) for byte in encoded_text)
            return decoded_string
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")
