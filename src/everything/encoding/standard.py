from everything.encoding.standard_modules.base64 import ME_EncodeBase64
from everything.encoding.standard_modules.base64 import ME_DecodeBase64
from everything.encoding.standard_modules.hex import ME_EncodeHex
from everything.encoding.standard_modules.hex import ME_DecodeHex
from everything.encoding.standard_modules.binary import ME_EncodeBinary
from everything.encoding.standard_modules.binary import ME_DecodeBinary

class TELSEncoding():
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
            return ME_EncodeBase64(plaintext=plaintext, encoding=encoding)
        except UnicodeEncodeError as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "UnicodeEncodeError"
        except UnicodeDecodeError as msg:
            print(f"There was an error when decoding the text!\n{msg}")
            return "UnicodeDecodeError"
        except Exception as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "ERROR"
    
    def base64_decode(self, plaintext: str, encoding: str) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            return ME_DecodeBase64(plaintext=plaintext, encoding=encoding)
        except UnicodeEncodeError as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "UnicodeEncodeError"
        except UnicodeDecodeError as msg:
            print(f"There was an error when decoding the text!\n{msg}")
            return "UnicodeDecodeError"
        except Exception as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "ERROR"

    def hex_encode(self, plaintext: str, encoding: str = 'utf-8') -> str:
        '''
        WIP! Coming soon
        '''
        try:
            return ME_EncodeHex(plaintext=plaintext, encoding=encoding)
        except UnicodeEncodeError as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "UnicodeEncodeError"
        except UnicodeDecodeError as msg:
            print(f"There was an error when decoding the text!\n{msg}")
            return "UnicodeDecodeError"
        except Exception as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "ERROR"
    
    def hex_decode(self, encoded_text: str, encoding: str) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            return ME_DecodeHex(encoded_text=encoded_text, encoding=encoding)
        except UnicodeEncodeError as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "UnicodeEncodeError"
        except UnicodeDecodeError as msg:
            print(f"There was an error when decoding the text!\n{msg}")
            return "UnicodeDecodeError"
        except Exception as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "ERROR"
        
    def binary_encode(self, plaintext: str, as_bytes: bool = False) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            return ME_EncodeBinary(plaintext=plaintext, as_bytes=as_bytes)
        except UnicodeEncodeError as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "UnicodeEncodeError"
        except UnicodeDecodeError as msg:
            print(f"There was an error when decoding the text!\n{msg}")
            return "UnicodeDecodeError"
        except Exception as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "ERROR"
    
    def binary_decode(self, encoded_text: str) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            return ME_DecodeBinary(encoded_text=encoded_text)
        except UnicodeEncodeError as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "UnicodeEncodeError"
        except UnicodeDecodeError as msg:
            print(f"There was an error when decoding the text!\n{msg}")
            return "UnicodeDecodeError"
        except Exception as msg:
            print(f"There was an error when encoding the text!\n{msg}")
            return "ERROR"
