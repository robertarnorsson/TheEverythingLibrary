from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

setup(
    name="The Everything Library",
    version="0.4.0",
    description="Library with a module for almost everything",
    url="https://github.com/RobertArnosson/TheEverythingLibrary",
    author="Robert Arnorsson",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires= [
        "cryptography",
        "uuid"
    ],
    python_requires=">=3.9",
    project_urls={
        "Bug Reports": "https://github.com/RobertArnosson/TheEverythingLibrary/issues",
        "Source": "https://github.com/RobertArnosson/TheEverythingLibrary",
    },
)