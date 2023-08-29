import os
from theeverythinglibrary.expetions import InvalidColor

def cprint(text: str, color=None, bg_color=None):
    '''
    WIP! Coming soon
    '''
    COLORS = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
    }
    
    RESET = '\033[0m'

    if color != None and color not in COLORS:
        raise InvalidColor(color=color)
    
    # Check if the specified colors are valid
    background_code = str(int(COLORS.get(bg_color, '')) + 10) if bg_color != None else "0"
    text_code = COLORS.get(color, '') if color != None else "0"
    
    colored_text = f'\033[{background_code};{text_code}m{text}{RESET}'
    
    print(colored_text)


class TELUtilities:
    '''
    WIP! Coming soon
    '''
    def __init__(self) -> None:
        pass

    def project_path(self):
        '''
        WIP! Coming soon
        '''
        return os.path.abspath(os.path.dirname(__file__))

    def project_file_path(self):
        '''
        WIP! Coming soon
        '''
        return os.path.abspath(os.path.abspath(__file__))