import os
import re
import shutil
import datetime

class TELFileManager:
    '''
    ## File Manager
    ---
    This class provides utility functions for managing files and directories.

    **Note:** This class is a work in progress and subject to further development.
    '''

    class File:
        '''
        ## File Class
        ---
        ### Description
        Represents a file with various attributes such as name, extension, path, size, permissions, user ID, group ID,
        last access time, last modification time, and creation time.\n
        ---
        ### Constructor
        - `name`: The name of the file.
        - `extension`: The file extension (not including the dot).
        - `path`: The path to the file.
        - `size`: The size of the file in bytes.
        - `permissions`: The file's permissions or access rights.
        - `user_id`: The user ID of the file owner.
        - `group_id`: The group ID of the file owner's group.
        - `last_access_time`: The timestamp of the last access to the file.
        - `last_modification_time`: The timestamp of the last modification of the file.
        - `creation_time`: The timestamp of the file's creation.
        '''
        def __init__(self, name, extension, file_type, path, size, permissions, user_id, group_id, last_access_time, last_modification_time, creation_time) -> None:
            self.name = name
            self.extension = extension
            self.file_type = file_type
            self.path = path
            self.size = size
            self.permissions = permissions
            self.user_id = user_id
            self.group_id = group_id
            self.last_access_time = last_access_time
            self.last_modification_time = last_modification_time
            self.creation_time = creation_time
        
        def display(self):
            '''
            ## Display
            ---
            ### Description
            Prints info about a `File` class to the console.\n
            ---
            ### Arguments
                - None\n
            ---
            ### Return
                - None.\n
            ---
            ### Exceptions
                - None\n
            '''
            print(f'---------------------- | Info for "{self.name}" | ----------------------')
            print(f'Name:                     {self.name}')
            print(f'Extension:                {self.extension}')
            print(f'File Type:                {self.file_type}')
            print(f'Path:                     {self.path}')
            print(f'Size:                     {self.size} bytes | {round(self.size / 1024, 4)} KB | {round(self.size / (1024 * 1024), 4)} MB | {round(self.size / (1024 * 1024 * 1024), 4)} GB')
            print(f'Permissions:              {self.permissions}')
            print(f'User ID:                  {self.user_id}')
            print(f'Group ID:                 {self.group_id}')
            print(f'Last Access Time:         {self.last_access_time}')
            print(f'Last Modification Time:   {self.last_modification_time}')
            print(f'Creation Time:            {self.creation_time}')
    
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

    def search(self, dir: str, extensions: list[str] = None, keywords: list[str] = None,
            exclude_extensions: list[str] = None, exclude_keywords: list[str] = None,
            exclude_dirs: list[str] = None, max_depth: int = None,
            min_size: int = None, max_size: int = None,
            list_empty_dirs: bool = False, divider: str = "\\"):
        '''
        ## Search Files
        ---
        ### Description
        Recursively search for files in a directory based on specified criteria.\n
        ---
        ### Arguments
            - `dir`: The directory in which to start the search.
            - `extensions`: A list of file extensions to filter by (optional).
            - `keywords`: A list of keywords to filter files by name (optional).
            - `exclude_extensions`: A list of file extensions to exclude (optional).
            - `exclude_keywords`: A list of keywords to exclude from file names (optional).
            - `exclude_dirs`: A list of directory names to exclude (optional).
            - `max_depth`: The maximum depth of recursion in the file structure (optional).
            - `min_size`: The minimum file size in bytes (optional).
            - `max_size`: The maximum file size in bytes (optional).
            - `list_empty_dirs`: Whether to list directories even if there are no files in them (optional).
            - `divider`: The directory separator character (optional).
        ---
        ### Return
            - A list of file paths that meet the specified search criteria.\n
        ---
        ### Exceptions
            - If an error occurs during searching.\n
        '''
        try:
            dir = dir.replace("/", "\\")

            if extensions:
                new_extensions = []
                for extension in extensions:
                    extension.replace(".", "")
                    if re.match(r'[a-zA-Z0-9]+$', extension):
                        new_extensions.append(extension)
                    else:
                        print(f'"{extension}" is not a valid extension')
                        continue
                extensions = new_extensions

            found_files = []
            found_empty_dirs = []  # Store empty directories if list_empty_dirs is True.

            for root, dirs, files in os.walk(dir):
                # Calculate the depth of the current directory.
                depth = root[len(dir):].count(os.path.sep)

                # Check if the current directory should be excluded based on depth.
                if max_depth is not None and depth > max_depth:
                    continue

                print(files)
                print(dir)
                print(root)

                # Check if the current directory should be excluded based on name.
                if exclude_dirs and not any(exclude_dir in dirs for exclude_dir in exclude_dirs):
                    continue

                if len(files) == 0:
                    if list_empty_dirs:
                        found_empty_dirs.append(root)
                else:
                    for file in files:
                        file_path = os.path.join(root, file)
                        file_size = os.path.getsize(file_path)

                        # Check if the file should be excluded based on extensions or keywords.
                        if (exclude_extensions and any(file.endswith(ext) for ext in exclude_extensions)) or \
                        (exclude_keywords and any(keyword in file for keyword in exclude_keywords)):
                            continue

                        # Check if the file meets the inclusion criteria.
                        if extensions and not any(file.endswith(ext) for ext in extensions):
                            continue

                        if keywords and not all(keyword in file for keyword in keywords):
                            continue

                        if min_size is not None and file_size < min_size:
                            continue

                        if max_size is not None and file_size > max_size:
                            continue

                        found_files.append(file_path)

            new_found_files = []
            new_found_empty_dirs = []

            for file_path in found_files:
                file_path = file_path.replace("\\", divider)
                new_found_files.append(file_path)
            
            for empty_dir in found_empty_dirs:
                empty_dir = empty_dir.replace("\\", divider)
                new_found_empty_dirs.append(empty_dir)

            if list_empty_dirs:
                new_found_files.extend(new_found_empty_dirs)

            return new_found_files
        except Exception as e:
            raise Exception(f"Something went wrong: {e}")

    def info(self, file) -> File:
        '''
        ## File info
        ---
        ### Description
        Get info about a file.\n
        ---
        ### Arguments
            - `file`: The file to get the info from.\n
        ---
        ### Return
            - A list of file paths that meet the specified search criteria.\n
        ---
        ### Exceptions
            - If an error occurs during searching.\n
        '''
        if not os.path.exists(file):
            raise Exception(f'"{file}" is not a valid file or the file was not found.')
        
        stat_info = os.stat(file)

        file_info = self.File(
            name = os.path.basename(file),
            extension = str(os.path.basename(file)).split(".")[-1] if os.path.isfile(os.path.abspath(file)) else "Folder",
            file_type = "File" if os.path.isfile(os.path.abspath(file)) else "Folder",
            path = os.path.abspath(file),
            size = stat_info.st_size,
            permissions = stat_info.st_mode,
            user_id = stat_info.st_uid,
            group_id = stat_info.st_gid,
            last_access_time = datetime.datetime.fromtimestamp(stat_info.st_atime).strftime('%Y-%m-%d %H:%M:%S'),
            last_modification_time = datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            creation_time = datetime.datetime.fromtimestamp(stat_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
        )

        return file_info
    
    def convert(self, bytes: int, unit: str, decimals: int = 4) -> float:
        '''
        ## Convert Bytes
        ---
        ### Description
        Converts a given number of bytes into specified units (e.g., kilobytes, megabytes, gigabytes) with a specified number of decimal places.\n
        ---
        ### Arguments
        - `bytes`: The number of bytes to convert.
        - `unit`: The target unit to convert to (options: 'bytes', 'kb', 'mb', 'gb').
        - `decimals`: The number of decimal places in the result (optional).\n
        ---
        ### Return
        - The converted size in the specified unit with the specified number of decimal places.\n
        ---
        ### Exceptions
        - `Exception`: Raised if an invalid unit is provided.\n
        '''
        unit = unit.lower().strip()
        conversion_factors = {
            'bytes': 1,
            'kb': 1024,
            'mb': 1024 * 1024,
            'gb': 1024 * 1024 * 1024
        }

        if unit not in conversion_factors:
            raise Exception(f'"{unit}" is not a valid unit. Units: (bytes, kb, mb, gb)')

        converted_size = bytes / conversion_factors[unit]
        return round(converted_size, decimals)