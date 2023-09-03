from googletrans import Translator, LANGUAGES

class TELTranslator:
    '''
    ## Translator
    ---
    This class provides utility functions for translating text to a different language.\n
    Use googletranse verion 3.1.0a0 (pip install googletrans==3.1.0a0)

    **Note:** This class is a work in progress and subject to further development.
    '''
    
    def __init__(self):
        self.gtranslator = Translator()

    def translat(self, text: str, source_language: str = "auto", target_language: str = "en") -> str:
        '''
        ## Translate
        ---
        ### Description
        Translates a given text from the source language to the target language.\n
        ---
        ### Arguments
            - `text`: The text to be translated.
            - `source_language`: The source language of the text. Default is "auto".
            - `target_language`: The target language for translation. Default is "en".\n
        ---
        ### Return
            - The translated text in the target language.\n
        ---
        ### Exceptions
            - If an error occurs during translation.\n
        '''
        try:
            translated = self.gtranslator.translate(text=text, src=source_language, dest=target_language)
            return translated.text
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
    
    def get_languages(self) -> dict:
        '''
        ## Get Supported Languages
        ---
        ### Description
        Retrieves the list of supported languages for translation.\n
        ---
        ### Return
            - A dictionary containing the language codes as keys and their corresponding names as values.\n
        '''
        return LANGUAGES