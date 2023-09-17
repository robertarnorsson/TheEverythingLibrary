<br/>
<div align="center">
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://raw.githubusercontent.com/RobertArnosson/TheEverythingLibraryAssets/main/TELLogo-780x240.png"></a>
<br/>
<br/>
<br/>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/v/theeverythinglibrary?style=for-the-badge&logo=pypi&logoColor=%2327CC88&label=Version&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/badge/python-3.9%2B-green?style=for-the-badge&logo=python&logoColor=%2327CC88&label=Python&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://github.com/RobertArnosson/TheEverythingLibrary" target="_blank"><img src="https://img.shields.io/github/stars/RobertArnosson/TheEverythingLibrary?style=for-the-badge&logo=github&logoColor=%2327CC88&label=Stars&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://pypistats.org/packages/theeverythinglibrary" target="_blank"><img src="https://img.shields.io/pypi/dm/theeverythinglibrary?style=for-the-badge&logo=docusign&logoColor=%2327CC88&label=Downloads&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/status/theeverythinglibrary?style=for-the-badge&logoColor=%2327CC88&label=Status&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/l/theeverythinglibrary?style=for-the-badge&logoColor=%2327CC88&label=License&labelColor=%23061122&color=%2327CC88"></a>
</div>
<br/>
<br/>

----------

# Installation
How to install the library 
```bash
pip install theeverythinglibrary
```
\
How to upgrade the library 
```bash
pip install --upgrade theeverythinglibrary
```
\
How to uninstall the library 
```bash
pip uninstall theeverythinglibrary
```

# How to use
Import the library
```python
import theeverythinglibrary
```

Find what you need
```python
from theeverythinglibrary.encoding import TELEncoding
from theeverythinglibrary.encryption import TELSymmetric, TELAsymmetric
from theeverythinglibrary.enviroment import TELEnviroment
from theeverythinglibrary.exceptions import InvalidFilenameError, InvalidColor
from theeverythinglibrary.files import TELFileManager
from theeverythinglibrary.hashing import TELHash
from theeverythinglibrary.math import TELMath
from theeverythinglibrary.regex import TELRegex
from theeverythinglibrary.sorting import TELSorting, TELSearching
from theeverythinglibrary.translator import TELTranslator
from theeverythinglibrary.utilities import TELUtilities
from theeverythinglibrary.web import TELHTTP
```

Then use it like this!
```python
from theeverythinglibrary.encoding import TELEncoding

encoding = TELEncoding()

encoded_text = encoding.hex_encode("Hello World!")

print(encoded_text)
>>> 48656c6c6f20576f726c6421

decoded_text = encoding.hex_decode(encoded_text)

print(decoded_text)
>>> Hello World!
```

# Features
### Encoding
- Base64 encoding and decoding
- Hex encoding and decoding
- Binary encoding and decoding

### Encryption
- Symmetric encryption
- Asymmetric encryption
- Public and Private key managment

### Enviroment variables
- Set variable
- Get variable
- Remove variable
- List all variables
- Does variable exist
- Get multiple variables
- Update variable
- Append variable
- Prepend variable
- Restore variable

### File Managment
- Create file
- Create directory
- Delete file
- Delete directory
- List files in directory
- Copy file to directory
- Copy files from one directory to different directory
- Move file to directory
- Move files from one directory to different directory
- Advanced recursive file searching

### Hashing
- Generate salt
- Hash a password
- Verify a hash
- Hash a file

### Math Functions
- Add two numbers
- Add list of numbers
- Subtract two numbers
- Subtract list of numbers
- Find average from list of numbers
- Find median from list of numbers

### Password
- Set password policy
- Generate password
- Check password with policy

### Regular expression
- Match
- Search
- Find all
- Replace
- Escape
- Split

### Sorting algorithms
- Bubble sort
- Selection sort
- Insertion sort
- Quick sort
- Merge sort
- Bogo sort

### Searching algorithms
- Search
- Linear search
- Binary search

### Translator
- Translate
- Get available languages

### Utilities
- Colored print
- Project path
- Project file path

### Web
- Get http request
- Post http request
- Put http request
- Delete http request
- Download file
- Get status codes

## Do you want to contribute?
Please try and use the formatting rules from the [FORMATTING.md](https://github.com/RobertArnosson/TheEverythingLibrary/blob/main/FORMATTING.md) file

## Visit Github for more info
[Visit the GitHub repository](https://github.com/RobertArnosson/TheEverythingLibrary) for the latest updates, documentation, and community discussions.

# History

0.0.1 (2023-08-26)
------------------

* Public on PyPi (pip install theeverythinglibrary)

0.0.2 - 0.0.7 (2023-08-26)
------------------

* Fixing import

0.1.0 (2023-08-26)
------------------

* Fixed import
* Added math functions
* Added sorting algorithms

0.2.0 (2023-08-27)
------------------

* Added more math functions
* Added file managment
* Reworked error handling

0.2.1 (2023-08-27)
------------------

* Fixed file manager args

0.2.2 (2023-08-27)
------------------

* Updated README

0.2.3 (2023-08-27)
------------------

* Fix with base64 decode args

0.2.4 (2023-08-27)
------------------

* Added searching algorithms

0.2.5 (2023-08-28)
------------------

* Fixed some small issues
* Added regular expressions (regex)

0.2.6 (2023-08-28)
------------------

* Fixed some small issues
* Added utilities
* Added an example of "Project Formatting and Guidelines" file (FORMATTING.md)

0.2.7 (2023-08-29)
------------------

* Added more functions for the file manager
    - Create file
    - Delete file
* Fixed cprint

0.2.8 (2023-08-29)
------------------

* Huge README change

0.3.0 (2023-08-30)
------------------

* Updated README
* Added environment variables utility
* Added managing and sending http requests
* Added more documentation

0.3.1 (2023-08-30)
------------------

* Updated README
* Added more documentation

0.3.2 (2023-08-31)
------------------

* Added translation
* Added file search

0.3.3 (2023-09-01)
------------------

* Improved file search
* Added file info
* Added class `File`
* Added byte converter

0.3.4 - 0.3.5 (2023-09-03)
------------------

* Cleanup

0.3.6 (2023-09-04)
------------------

* Rewrote file search for improved performance (works but might find bugs)

0.3.7 (2023-09-11)
------------------

* Fixes to file search
* Fixed some regex

0.3.8 (2023-09-12)
------------------

* Added hashing support

0.3.9 (2023-09-14)
------------------

* Fixes to hashing and setup requirements

0.3.10 (2023-09-17)
------------------

* Fixed and improvements to encoding
* Added copy dir
* Added move dir

0.3.11 (2023-09-17)
------------------

* Added `@staticmethod` to any function that supports it

0.3.12 (2023-09-17)
------------------

* Added password generation
* Added password policy
* Added password policy checking

------------------
<br>
<br>
<div align="center">
<h2>Hope you enjoy!</h2>
</div>