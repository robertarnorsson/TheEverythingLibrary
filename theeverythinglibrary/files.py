import os
import re
import shutil

class TELFileManager:
    '''
    WIP! Coming soon
    '''
    def __init__(self) -> None:
        pass

    def create_directory(self, dir: str) -> str:
        '''
        WIP! Coming soon
        '''
        try:
            os.makedirs(dir, exist_ok=True)
            return dir
        except OSError as e:
            raise OSError(f"Error creating directory: {e}")
        except Exception as e:
            raise Exception(f"Error deleting directory: {e}")

    def delete_directory(self, dir: str) -> bool:
        '''
        WIP! Coming soon
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
        WIP! Coming soon
        '''
        dir = dir.replace("/", "\\")
        type.replace(".", "")
        if not re.match(r'^[a-zA-Z0-9_]+\.[a-z]+$', f'{name}.{type}'):
            raise Exception(f'The file name "{name+"."+type}" is not a valid file name')
        try:
            with open(os.path.join(dir, f'{name}.{type}'), 'w+') as file:
                file.close()
        except Exception as e:
            raise Exception(f"Error ceating file: {e}")
    
    def delete_file(self, file: str) -> None:
        '''
        WIP! Coming soon
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
        WIP! Coming soon
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
        WIP! Coming soon
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
        WIP! Coming soon
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