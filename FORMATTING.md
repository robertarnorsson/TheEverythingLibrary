# **THIS FILE IS NOT IN USE YET AND IS A SUBJECT TO CHANGE!**

# Project Formatting and Guidelines

This document outlines the necessary formatting standards and provides clear instructions on maintaining code quality within the project.

## General Formatting Guidelines

### Consistent Indentation and Whitespace

* Maintain consistent indentation (spaces or tabs) throughout the codebase.
* Avoid mixing spaces and tabs within the same file.
* Use an indentation style (e.g., 4 spaces) that enhances readability.

Example:
```python
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    return total
```

### Meaningful Variable and Function Names

* Use descriptive and meaningful names for variables, functions, and classes.
* Names should reflect the purpose or functionality of the entity.
* Avoid single-letter variable names except in specific cases.

Example:
```python
def calculate_area(width, height):
    return width * height
```

### Limit Line Length

* Keep lines of code reasonably short (e.g., 80-100 characters) to prevent horizontal scrolling.
* Exception: Long URLs, paths, or comments can exceed this limit.

Example:
```python
long_url = "https://example.com/this-is-a-really-long-url-that-needs-to-be-handled"
```

### Comments and Documentation

* Provide comments for complex algorithms, non-intuitive logic, and potential pitfalls.
* Include documentation for public functions, explaining their purpose, expected inputs, and outputs.
* Use consistent and clear language in comments and documentation.

Example:
```python
def divide(a: int | float, b: int | float) -> float:
    '''
    ## Divide
    ---
    ### Description
    Divide two numbers.\n
    ---
    ### Arguments
        - `a`: The first number.
        - `b`: The second number.\n
    ---
    ### Return
        - The devided number.\n
    ---
    ### Exeptions
        - `ZeroDivisionError`: Can't divide by zero.
        - `TypeError`: Only "int" and "float" is supported.
        - `Exception`: The fallback error message.
    '''
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError('Can not divide by zero!')
    except TypeError:
        raise TypeError(f'"{type(a).__name__}" can not devide with "{type(b).__name__}"')
    except Exception as e:
        raise Exception(f'Something went wrong!\n{e.with_traceback()}')
```

### Modularization

* Break down code into smaller, reusable modules or functions.
* Follow the Single Responsibility Principle (SRP) for better maintainability.
* Encourage reusing existing code rather than duplicating it.

Example:
```python
# module_utils.py
def validate_email(email):
    # validation logic
    pass

# main.py
from module_utils import validate_email

user_email = input("Enter your email: ")
if validate_email(user_email):
    print("Email is valid.")
else:
    print("Email is not valid.")
```

### Consistent Naming Conventions

* Specify naming conventions for classes, functions, variables, and constants.
* Ensure naming is consistent across the project to facilitate collaboration.

Example:
```python
class MyClass:
    pass

def calculate_total_price(items):
    pass

MAX_RETRY_ATTEMPTS = 3
```

## Conclusion

By adhering to these guidelines, we ensure consistent code quality, readability, and maintainability throughout the project. Please refer to this document as a reference for maintaining the project's coding standards.
