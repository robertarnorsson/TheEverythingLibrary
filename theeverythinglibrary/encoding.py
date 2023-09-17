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

    def binary_encode(self, plaintext: str, as_bytes: bool = False, chunk_size: int = 8) -> str | bytes:
        '''
        ## Binary Encode
        ---
        ### Description
        Encode the given plaintext into binary representation.\n
        ---
        ### Arguments
            - `plaintext`: The text to encode.
            - `as_bytes` (optional): If `True`, return the encoded result as bytes (default is `False`).\n
            - `chunk_size` (optional): Size of each binary chunk (default is 8 bits).\n
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
                binary_str = ''.join(format(ord(char), '08b') for char in plaintext)
                if chunk_size > 0:
                    chunks = [binary_str[i:i+chunk_size] for i in range(0, len(binary_str), chunk_size)]
                    encoded_bytes = ' '.join(chunks)
                else:
                    encoded_bytes = binary_str
            return encoded_bytes
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def binary_decode(self, encoded_text: str | bytes, as_text: bool = True, chunk_size: int = 8) -> str:
        '''
        ## Binary Decode
        ---
        ### Description
        Decode binary data into text representation.\n
        ---
        ### Arguments
            - `encoded_text`: The binary data to decode (either string or bytes).
            - `as_text` (optional): If `True`, return the decoded result as text (default is `True`).\n
            - `chunk_size` (optional): Size of each binary chunk (default is 8 bits).\n
        ---
        ### Return
            - The decoded result as text.\n
        ---
        ### Exceptions
            - If an error occurs during decoding.\n
        '''
        try:
            if isinstance(encoded_text, bytes):
                binary_str = ''.join(format(byte, '08b') for byte in encoded_text)
            else:
                binary_str = ''.join(encoded_text.split())

            if chunk_size > 0:
                chunks = [binary_str[i:i+chunk_size] for i in range(0, len(binary_str), chunk_size)]
            else:
                chunks = [binary_str]

            decoded_text = ''.join([chr(int(chunk, 2)) for chunk in chunks])

            return decoded_text if as_text else decoded_text.encode('utf-8')
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

