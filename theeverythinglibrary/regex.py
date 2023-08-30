import re

class TELRegex:
    '''
    ## Regex
    ---
    This class provides utility functions for regular expressions (regex).

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self, default_pattern):
        '''
        ## Constructor
        ---
        ### Description
        Initialize the TELRegex utility with a default pattern.\n
        ---
        ### Arguments
            - `default_pattern`: The default regex pattern used in methods when no specific pattern is provided.\n
        '''
        self.default_pattern = default_pattern

        self.common_patterns = {
            "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',
            "url": r'https?://(?:www\.)?[A-Za-z0-9.-]+(?:\.[A-Za-z]{2,})+[\w/]*',
            "date": r'\d{4}-\d{2}-\d{2}',
            "phone": r'\b(?:\+\d{1,2}\s?)?(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}\b',
            "ip": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            "color": r'#[0-9A-Fa-f]{6}',
            "word": r'\b\w+\b',
            "text": r'[a-z]+',
            "number": r'\d+(?:\.\d+)?'
        }
    
    def pattern(self, name: str):
        '''
        ## Pattern
        ---
        ### Description
        Retrieve a common regex pattern by name.\n
        ---
        ### Arguments
            - `name`: The name of the common pattern to retrieve.\n
        ---
        ### Return
            - The requested regex pattern.\n
        ---
        ### Exceptions
            - If the provided `name` is not a valid common pattern name.\n
        '''
        try:
            return self.common_patterns[name.lower()]
        except KeyError:
            raise KeyError(f'The name "{name}" is not a valid name. Please choose a name from this list: email, url, date, phone, ip, color, word, text, number')
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def match(self, text, pattern=None):
        '''
        ## Match
        ---
        ### Description
        Match a pattern at the beginning of the text.\n
        ---
        ### Arguments
            - `text`: The text to match against.
            - `pattern` (optional): The regex pattern to use for matching (default is the default pattern).\n
        ---
        ### Return
            - The match object or `None` if no match is found.\n
        ---
        ### Exceptions
            - If an error occurs during matching.\n
        '''
        try:
            pattern_to_use = pattern if pattern is not None else self.default_pattern
            return re.match(pattern_to_use, text)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def search(self, text, pattern=None):
        '''
        ## Search
        ---
        ### Description
        Search for a pattern within the text.\n
        ---
        ### Arguments
            - `text`: The text to search within.
            - `pattern` (optional): The regex pattern to use for searching (default is the default pattern).\n
        ---
        ### Return
            - The match object or `None` if no match is found.\n
        ---
        ### Exceptions
            - If an error occurs during searching.\n
        '''
        try:
            pattern_to_use = pattern if pattern is not None else self.default_pattern
            return re.search(pattern_to_use, text)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def findall(self, text, pattern=None):
        '''
        ## Find All
        ---
        ### Description
        Find all occurrences of a pattern within the text.\n
        ---
        ### Arguments
            - `text`: The text to search within.
            - `pattern` (optional): The regex pattern to use for finding (default is the default pattern).\n
        ---
        ### Return
            - A list of matched substrings.\n
        ---
        ### Exceptions
            - If an error occurs during finding.\n
        '''
        try:
            pattern_to_use = pattern if pattern is not None else self.default_pattern
            return re.findall(pattern_to_use, text)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def finditer(self, text, pattern=None):
        '''
        ## Find Iter
        ---
        ### Description
        Find all occurrences of a pattern within the text and return an iterator over match objects.\n
        ---
        ### Arguments
            - `text`: The text to search within.
            - `pattern` (optional): The regex pattern to use for finding (default is the default pattern).\n
        ---
        ### Return
            - An iterator over match objects.\n
        ---
        ### Exceptions
            - If an error occurs during finding.\n
        '''
        try:
            pattern_to_use = pattern if pattern is not None else self.default_pattern
            return re.finditer(pattern_to_use, text)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def replace(self, text, replacement, pattern=None):
        '''
        ## Replace
        ---
        ### Description
        Replace occurrences of a pattern in the text with a specified replacement.\n
        ---
        ### Arguments
            - `text`: The text to perform replacement on.
            - `replacement`: The replacement string.
            - `pattern` (optional): The regex pattern to use for replacement (default is the default pattern).\n
        ---
        ### Return
            - The text with replacements.\n
        ---
        ### Exceptions
            - If an error occurs during replacement.\n
        '''
        try:
            pattern_to_use = pattern if pattern is not None else self.default_pattern
            return re.sub(pattern_to_use, replacement, text)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    @staticmethod
    def escape(text):
        '''
        ## Escape
        ---
        ### Description
        Escape special characters in a text so they can be used as literals in regex patterns.\n
        ---
        ### Arguments
            - `text`: The text to escape.\n
        ---
        ### Return
            - The escaped text.\n
        ---
        ### Exceptions
            - If an error occurs during escaping.\n
        '''
        try:
            return re.escape(text)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    @staticmethod
    def split(text, pattern):
        '''
        ## Split
        ---
        ### Description
        Split a text into substrings using a specified regex pattern as the delimiter.\n
        ---
        ### Arguments
            - `text`: The text to split.
            - `pattern`: The regex pattern to use as the delimiter.\n
        ---
        ### Return
            - A list of substrings.\n
        ---
        ### Exceptions
            - If an error occurs during splitting.\n
        '''
        try:
            return re.split(pattern, text)
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")
