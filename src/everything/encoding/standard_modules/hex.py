def ME_EncodeHex(plaintext: str, encoding: str) -> str:
    '''
    WIP! Coming soon
    '''
    encoded_string = plaintext.encode(encoding=encoding).hex()
    return encoded_string

def ME_DecodeHex(encoded_text: str, encoding: str) -> str:
    '''
    WIP! Coming soon
    '''
    decoded_string = bytes.fromhex(encoded_text).decode(encoding=encoding)
    return decoded_string
