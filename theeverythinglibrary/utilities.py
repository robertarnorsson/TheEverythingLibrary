import os
from theeverythinglibrary.exceptions import InvalidColor

def cprint(text: str, color=None, bg_color=None):
    '''
    ## Print Colored Text
    ---
    ### Description
    Print text in the terminal with specified foreground and background colors.\n
    ---
    ### Arguments
        - `text`: The text to be printed.
        - `color`: The desired text color. Available colors: 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.
        - `bg_color`: The desired background color. Available colors: 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.\n
    ---
    ### Exceptions
        - If an invalid color name is provided, raises `InvalidColor`.\n
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
    
    background_code = str(int(COLORS.get(bg_color, '')) + 10) if bg_color != None else "0"
    text_code = COLORS.get(color, '') if color != None else "0"
    
    colored_text = f'\033[{background_code};{text_code}m{text}{RESET}'
    
    print(colored_text)


class TELUtilities:
    '''
    ## Utilities
    ---
    This class provides usefull utility functions.

    **Note:** This class is a work in progress and subject to further development.
    '''
    def __init__(self) -> None:
        pass

    def project_path(self) -> str:
        '''
        ## Get Project Path
        ---
        ### Description
        Get the absolute path to the directory containing the current project.\n
        ---
        ### Return
            - The absolute path to the project directory.\n
        '''
        return os.path.abspath(os.path.dirname(__file__))

    def project_file_path(self) -> str:
        '''
        ## Get Project File Path
        ---
        ### Description
        Get the absolute path of the current script file within the project.\n
        ---
        ### Return
            - The absolute path to the script file.\n
        '''
        return os.path.abspath(os.path.abspath(__file__))