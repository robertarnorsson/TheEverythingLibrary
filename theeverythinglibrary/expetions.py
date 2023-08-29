class InvalidFilenameError(Exception):
    def __init__(self, filename):
        self.filename = filename
        self.message = f"'{filename}' is not a valid filename."
        super().__init__(self.message)

class InvalidColor(Exception):
    
    def __init__(self, color):
        self.color = color
        self.message = f'"{color}" is not a valid color!'
        super().__init__(self.message)