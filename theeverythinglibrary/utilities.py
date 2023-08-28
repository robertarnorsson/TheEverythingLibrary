import os

def cprint(text: str, text_color=None, background_color=None):
    '''
    WIP! Coming soon (Might not work as expected!)
    '''
    COLORS_F = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
    }

    COLORS_B = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47',
    }
    
    RESET = '\033[0m'
    
    # Check if the specified colors are valid
    background_code = COLORS_B.get(background_color, '')
    text_code = COLORS_F.get(text_color, '')
    
    colored_text = f'\033[{background_code};{text_code}m{text}{RESET}'
    
    print(colored_text)


class TELUtilities:
    '''
    WIP! Coming soon
    '''
    def __init__(self) -> None:
        pass

    def project_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def project_file_path(self):
        return os.path.abspath(os.path.abspath(__file__))