def ME_EncodeBinary(plaintext: str, as_bytes: bool = False) -> str | bytes:
    if as_bytes:
        encoded_bytes = bytes([ord(char) for char in plaintext])
    else:
        encoded_bytes = ' '.join(format(ord(char), '08b') for char in plaintext)
    return encoded_bytes

def ME_DecodeBinary(encoded_text: str | bytes) -> str:
    if type(encoded_text) == str:
        binary_list = encoded_text.split()
        decoded_string = ''.join(chr(int(binary, 2)) for binary in binary_list)
    elif type(encoded_text) == bytes:
        decoded_string = ''.join(chr(byte) for byte in encoded_text)
    return decoded_string