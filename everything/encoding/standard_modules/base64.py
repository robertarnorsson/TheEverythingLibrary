import base64

def ME_EncodeBase64(plaintext: str, encoding: str) -> str:
    """
    Encodes a string or bytes-like object into base64 format.
    
    Args:
        data: The input data to be encoded.
        
    Returns:
        The base64 encoded string.
    """
    encoded_bytes = base64.b64encode(plaintext.encode(encoding=encoding))
    encoded_string = encoded_bytes.decode(encoding=encoding)
    return encoded_string

def ME_DecodeBase64(plaintext: str, encoding: str) -> str:
    """
    Decodes a base64 encoded string into its original format.
    
    Args:
        encoded_text: The base64 encoded text.
        
    Returns:
        The decoded bytes.
    """
    decoded_bytes = base64.b64decode(plaintext.encode(encoding=encoding))
    decoded_string = decoded_bytes.decode(encoding=encoding)
    return decoded_string
