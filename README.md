<br/>
<div align="center">
<img src="https://raw.githubusercontent.com/RobertArnosson/TheEverythingLibraryAssets/main/TELLogo-800x250.png">
<br/>
<br/>
<br/>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/v/theeverythinglibrary?style=for-the-badge&logo=pypi&logoColor=%2327CC88&label=Version&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/badge/python-3.9%2B-green?style=for-the-badge&logo=python&logoColor=%2327CC88&label=Python&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/github/stars/RobertArnosson/TheEverythingLibrary?style=for-the-badge&logo=github&logoColor=%2327CC88&label=Stars&labelColor=%23061122&color=%2327CC88"></a>
<a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/dm/theeverythinglibrary?style=for-the-badge&logo=docusign&logoColor=%2327CC88&label=Downloads&labelColor=%23061122&color=%2327CC88"></a>
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
from theeverythinglibrary.math import TELMath
from theeverythinglibrary.regex import TELRegex
from theeverythinglibrary.sorting import TELSorting, TELSearching
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
## Current features
### Encoding
- Base64 encoding and decoding
- Hex encoding and decoding
- Binary encoding and decoding

### Encryption
- Symmetric encryption
- Asymmetric encryption
- Public and Private key managment

### File Managment
- Create directory
- Delete directory
- List files in directory
- Copy files from directory to different directory
- Move files from directory to different directory

### Math Functions
- Add two numbers
- Add list of numbers
- Subtract two numbers
- Subtract list of numbers
- Find average from list of numbers
- Find median from list of numbers

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

### Regular expression
- Match
- Search
- Find all
- Replace
- Escape
- Split

### Utilities
- Colored print
- Project path
- Project file path

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