import random
import string
import os
import re

class TELPassword:
    '''
    ## Password
    ---
    This class provides utility functions for password policies, password generation and passwor checks.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self, min_length: int = 8, require_uppercase: bool = True, require_lowercase: bool = True,
                 require_digit: bool = True, require_special_char: bool = True):
        '''
        ## Password
        ---
        This class provides utility functions for password policies, password generation and passwor checks.\n
        ---
        ### Arguments (sets the policy)
            - `min_length` (optional): Minimum allowed length of password (default is `8`).\n
            - `require_uppercase` (optional): Does the password require uppercase (default is `True`).\n
            - `require_lowercase` (optional): Does the password require lowercase (default is `True`).\n
            - `require_digit` (optional): Does the password require digits (default is `True`).\n
            - `require_special_char` (optional): Does the password require special characters (default is `True`).\n
        
        **Note:** This class is a work in progress and subject to further development.
        '''
        self.password_policy = {
            'min_length': min_length,
            'require_uppercase': require_uppercase,
            'require_lowercase': require_lowercase,
            'require_digit': require_digit,
            'require_special_char': require_special_char,
        }

    def set_policy(self, min_length: int = 8, require_uppercase: bool = True, require_lowercase: bool = True,
                   require_digit: bool = True, require_special_char: bool = True) -> None:
        """
        ## Set password policy
        ---
        ### Description
        Set a custom password policy for password.\n
        ---
        ### Arguments:
            - `min_length` (optional): Minimum password length (default is `8`).
            - `require_uppercase` (optional): Require uppercase letters (default is `True`).
            - `require_lowercase` (optional): Require lowercase letters (default is `True`).
            - `require_digit` (optional): Require at least one digit (default is `True`).
            - `require_special_char` (optional): Require at least one special character (default is `True`).
        ---
        ### Exceptions
            - If something went wrong during changing of password policy.\n
        """
        try:
            if min_length is not None:
                self.password_policy['min_length'] = min_length
            if require_uppercase is not None:
                self.password_policy['require_uppercase'] = require_uppercase
            if require_lowercase is not None:
                self.password_policy['require_lowercase'] = require_lowercase
            if require_digit is not None:
                self.password_policy['require_digit'] = require_digit
            if require_special_char is not None:
                self.password_policy['require_special_char'] = require_special_char
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def generate_password(self, length: int = 8, custom_characters: str = '', raise_error: bool = False) -> str | bool:
        '''
        ## Generate password
        ---
        ### Description
        Generate a random password based on the password policy or custom character regex.\n
        ---
        ### Arguments:
            - `length` (optional): Length of the generated password (default is `8`).\n
            - `custom_characters` (optional): Use custom characters (regex) instead of the normal ones (default is `''`). **Note:** This will override the password policy!\n
            - `raise_error` (optional): Should raise an error when the policy is not met (default is `True`).\n
        ---
        ### Return
            - The generated password or `False` if the policy was not met.\n
        ---
        ### Exceptions
            - If something went wrong during generation of a password.\n
        '''
        if length < self.password_policy['min_length']:
            if raise_error:
                raise ValueError(f"Password length must be at least {self.password_policy['min_length']} characters.")
            return False

        password = ''

        def urandom_choice(_list):
            # Generate random bytes from os.urandom
            random_bytes = os.urandom(8)  # You can adjust the number of bytes as needed

            # Convert the random bytes to an integer index
            index = int.from_bytes(random_bytes, byteorder='big') % len(_list)

            # Return the randomly selected item from the list
            return _list[index]

        # Ensure at least one character from each required category
        if self.password_policy['require_uppercase']:
            password += urandom_choice(string.ascii_uppercase)

        if self.password_policy['require_lowercase']:
            password += urandom_choice(string.ascii_lowercase)

        if self.password_policy['require_digit']:
            password += urandom_choice(string.digits)

        if self.password_policy['require_special_char']:
            password += urandom_choice(string.punctuation)

        remaining_length = max(0, length - len(password))

        # Use custom_characters if provided (as regex), otherwise use the default character sets
        if custom_characters:
            custom_characters_regex = re.compile(custom_characters)
            custom_characters_pool = ''.join(re.findall(custom_characters_regex, string.printable))
            password += ''.join(urandom_choice(custom_characters_pool) for _ in range(remaining_length))
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password += ''.join(urandom_choice(characters) for _ in range(remaining_length))

        password_list = list(password)
        random.shuffle(password_list)
        return ''.join(password_list)

    def check_password(self, password: str) -> bool:
        '''
        ## Check password complexity 
        ---
        ### Description
        Check the complexity of a password based on the password policy.\n
        ---
        ### Arguments:
            - `password`: The password to check.\n
        ---
        ### Return
            - `True` if the password meets the policy, `False` otherwise.\n
        ---
        ### Exceptions
            - If something went wrong during checking of password.\n
        '''
        if len(password) < self.password_policy['min_length']:
            return False
        if self.password_policy['require_uppercase'] and not any(c.isupper() for c in password):
            return False
        if self.password_policy['require_lowercase'] and not any(c.islower() for c in password):
            return False
        if self.password_policy['require_digit'] and not any(c.isdigit() for c in password):
            return False
        if self.password_policy['require_special_char'] and not any(c in string.punctuation for c in password):
            return False
        return True