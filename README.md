<div style="padding: 40px"></div>
<div style="position: relative; display: flex; align-items: center; justify-content: center; padding: 10px;">
    <p style="padding: 15px"><a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://github.com/RobertArnosson/TheEverythingLibraryAssets/blob/main/TELLogo-128xR.png?raw=true"></a></p>
    <div>
        <p style="font-size: 54px;">The Everything Library</p>
        <p style="font-size: 12px; position: absolute; transform: translate(7px, -22.5px);">Unlock the Power of Python with The Everything Library</p>
    </div>
</div>
<div style="display: flex; align-items: center; justify-content: center;">
    <p style="padding: 5px"><a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/v/theeverythinglibrary?label=Version"></a></p>
    <p style="padding: 5px"><a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/badge/python-3.9%2B-green?logo=python&logoColor=white&label=Python"></a></p>
    <p style="padding: 5px"><a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/github/stars/RobertArnosson/TheEverythingLibrary?logo=github&logoColor=white&label=Stars"></a></p>
    <p style="padding: 5px"><a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/dm/theeverythinglibrary?logo=pypi&logoColor=white&label=Downloads"></a></p>
    <p style="padding: 5px"><a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/status/theeverythinglibrary?label=Status"></a></p>
    <p style="padding: 5px"><a href="https://pypi.org/project/theeverythinglibrary/" target="_blank"><img src="https://img.shields.io/pypi/l/theeverythinglibrary?label=License"></a></p>
</div>
<div style="padding: 40px"></div>
<div style="display: flex; align-items: center; justify-content: center; flex-direction: column;">
    <p style="font-size: 32px; padding: 5px;">Description</p>
    <p style="font-size: 16px;">This Python Library will have a LOT of different helper functions and classes that you can use for your own projects.</p>
</div>
<div style="padding: 40px"></div>

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
from theeverythinglibrary.files import TELFileManager
from theeverythinglibrary.math import TELMath
from theeverythinglibrary.sorting import TELSorting
from theeverythinglibrary.regex import TELRegex
from theeverythinglibrary.utilities import TELUtilities
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
