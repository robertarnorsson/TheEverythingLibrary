import re

class TELRegex:
    def __init__(self, default_pattern):
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
        try:
            return self.common_patterns[name.lower()]
        except KeyError:
            raise KeyError(f'The name "{name}" is not a valid name. Please choose a name from this list: email, url, date, phone, ip, color, word, text, number')

    def match(self, text, pattern=None):
        pattern_to_use = pattern if pattern is not None else self.default_pattern
        return re.match(pattern_to_use, text)

    def search(self, text, pattern=None):
        pattern_to_use = pattern if pattern is not None else self.default_pattern
        return re.search(pattern_to_use, text)

    def findall(self, text, pattern=None):
        pattern_to_use = pattern if pattern is not None else self.default_pattern
        return re.findall(pattern_to_use, text)

    def finditer(self, text, pattern=None):
        pattern_to_use = pattern if pattern is not None else self.default_pattern
        return re.finditer(pattern_to_use, text)

    def replace(self, text, replacement, pattern=None):
        pattern_to_use = pattern if pattern is not None else self.default_pattern
        return re.sub(pattern_to_use, replacement, text)

    @staticmethod
    def escape(text):
        return re.escape(text)

    @staticmethod
    def split(text, pattern):
        return re.split(pattern, text)
    
default_pattern = r'\d+'
regex_util = TELRegex(default_pattern)

text = "There are 123 apples and 456 bananas."
matches = regex_util.findall(text)
print(matches)  # Output: ['123', '456']

custom_pattern = r'[a-z]+'
custom_matches = regex_util.search(text, pattern=regex_util.pattern('text'))
print(custom_matches)