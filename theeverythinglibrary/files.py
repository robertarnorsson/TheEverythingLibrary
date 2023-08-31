import os
import re
import shutil

class TELFileManager:
    '''
    ## File Manager
    ---
    This class provides utility functions for managing files and directories.

    **Note:** This class is a work in progress and subject to further development.
    '''
    
    def __init__(self) -> None:
        pass

    def create_directory(self, dir: str) -> str:
        '''
        ## Create Directory
        ---
        ### Description
        Create a directory if it doesn't exist.\n
        ---
        ### Arguments
            - `dir`: The directory path to create.\n
        ---
        ### Return
            - The created directory path.\n
        ---
        ### Exceptions
            - If an error occurs during directory creation.\n
        '''
        try:
            os.makedirs(dir, exist_ok=True)
            return dir
        except OSError as e:
            raise OSError(f"Error creating directory: {e}")
        except Exception as e:
            raise Exception(f"Error creating directory: {e}")

    def delete_directory(self, dir: str) -> bool:
        '''
        ## Delete Directory
        ---
        ### Description
        Delete a directory and its contents.\n
        ---
        ### Arguments
            - `dir`: The directory path to delete.\n
        ---
        ### Return
            - `True` if the directory was deleted successfully, otherwise `False`.\n
        ---
        ### Exceptions
            - If an error occurs during directory deletion.\n
        '''
        try:
            if os.path.exists(dir) and os.path.isdir(dir):
                shutil.rmtree(dir)
                return True
            return False
        except Exception as e:
            raise Exception(f"Error deleting directory: {e}")

    def create_file(self, dir: str, name: str, type: str) -> None:
        '''
        ## Create File
        ---
        ### Description
        Create a file in the specified directory.\n
        ---
        ### Arguments
            - `dir`: The directory path where the file will be created.
            - `name`: The name of the file.
            - `type`: The file type (extension).\n
        ---
        ### Exceptions
            - If the provided file name and type are not valid.\n
        '''
        dir = dir.replace("/", "\\")
        type.replace(".", "")
        if not re.match(r'^[a-zA-Z0-9_]+\.[a-z]+$', f'{name}.{type}'):
            raise Exception(f'The file name "{name+"."+type}" is not a valid file name')
        try:
            with open(os.path.join(dir, f'{name}.{type}'), 'w+') as file:
                file.close()
        except Exception as e:
            raise Exception(f"Error creating file: {e}")

    def delete_file(self, file: str) -> None:
        '''
        ## Delete File
        ---
        ### Description
        Delete a file.\n
        ---
        ### Arguments
            - `file`: The path of the file to delete.\n
        ---
        ### Exceptions
            - If the provided path does not lead to a valid file.\n
        '''
        file = file.replace("/", "\\")
        file_name = file.split('\\')[len(file.split('\\'))-1]
        if not os.path.isfile(file):
            raise Exception(f'"{file_name}" is not a valid file or path')
        try:
            os.remove(file)
        except Exception as e:
            raise Exception(f"Error deleting file: {e}")

    def list_files(self, dir: str) -> list[str]:
        '''
        ## List Files
        ---
        ### Description
        List all files in a directory.\n
        ---
        ### Arguments
            - `dir`: The directory path to list files from.\n
        ---
        ### Return
            - A list of file names in the directory.\n
        ---
        ### Exceptions
            - If an error occurs during listing.\n
        '''
        try:
            if os.path.exists(dir) and os.path.isdir(dir):
                files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
                return files
            return []
        except Exception as e:
            raise Exception(f"Error listing files: {e}")

    def copy_file(self, file: str, dest_dir: str) -> bool:
        '''
        ## Copy File
        ---
        ### Description
        Copy a file to a destination directory.\n
        ---
        ### Arguments
            - `file`: The path of the file to copy.
            - `dest_dir`: The destination directory path.\n
        ---
        ### Return
            - `True` if the file was copied successfully, otherwise `False`.\n
        ---
        ### Exceptions
            - If an error occurs during copying.\n
        '''
        file = file.replace("/", "\\")
        file_name = file.split('\\')[len(file.split('\\'))-1]
        path_to_file = file.replace(file_name, "")
        try:
            if os.path.exists(path_to_file) and os.path.isfile(file):
                shutil.copy(file, dest_dir)
                return True
            return False
        except Exception as e:
            raise Exception(f"Error copying file: {e}")

    def move_file(self, file: str, dest_dir: str) -> bool:
        '''
        ## Move File
        ---
        ### Description
        Move a file to a destination directory.\n
        ---
        ### Arguments
            - `file`: The path of the file to move.
            - `dest_dir`: The destination directory path.\n
        ---
        ### Return
            - `True` if the file was moved successfully, otherwise `False`.\n
        ---
        ### Exceptions
            - If an error occurs during moving.\n
        '''
        file = file.replace("/", "\\")
        file_name = file.split('\\')[len(file.split('\\'))-1]
        path_to_file = file.replace(file_name, "")
        try:
            if os.path.exists(path_to_file) and os.path.isfile(file):
                shutil.move(file, dest_dir)
                return True
            return False
        except Exception as e:
            raise Exception(f"Error moving file: {e}")
    
    def search(self, dir: str, extensions: list = None, keywords=None, min_size=None, max_size=None):
        found_files = []

        for root, _, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)

                if extensions and not any(file.endswith(ext) for ext in extensions):
                    continue

                if keywords and not all(keyword in file for keyword in keywords):
                    continue

                if min_size is not None and file_size < min_size:
                    continue

                if max_size is not None and file_size > max_size:
                    continue

                found_files.append(file_path)

        return found_files

fm = TELFileManager()

files = fm.search('C:\\')
print(files)
print(len(files))