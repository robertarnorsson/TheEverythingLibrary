import os
import shutil

class TELFileManager:
    def create_directory(self, base_dir: str, dir_name: str) -> str:
        dir_path = os.path.join(base_dir, dir_name)
        try:
            os.makedirs(dir_path, exist_ok=True)
            return dir_path
        except OSError as msg:
            raise OSError(f"Error creating directory: {msg}")
        except Exception as msg:
            raise Exception(f"Error deleting directory: {msg}")

    def delete_directory(self, base_dir: str, dir_name: str) -> bool:
        dir_path = os.path.join(base_dir, dir_name)
        try:
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                shutil.rmtree(dir_path)
                return True
            return False
        except Exception as msg:
            raise Exception(f"Error deleting directory: {msg}")

    def list_files(self, base_dir: str, dir_name: str) -> list[str]:
        dir_path = os.path.join(base_dir, dir_name)
        try:
            if os.path.exists(dir_path) and os.path.isdir(dir_path):
                files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
                return files
            return []
        except Exception as msg:
            raise Exception(f"Error listing files: {msg}")

    def copy_file(self, base_dir: str, src_dir: str, src_file: str, dest_dir: str) -> bool:
        src_path = os.path.join(base_dir, src_dir, src_file)
        dest_path = os.path.join(base_dir, dest_dir, src_file)
        try:
            if os.path.exists(src_path) and os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
                return True
            return False
        except Exception as msg:
            raise Exception(f"Error copying file: {msg}")

    def move_file(self, base_dir: str, src_dir: str, src_file: str, dest_dir: str) -> bool:
        src_path = os.path.join(base_dir, src_dir, src_file)
        dest_path = os.path.join(base_dir, dest_dir, src_file)
        try:
            if os.path.exists(src_path) and os.path.isfile(src_path):
                shutil.move(src_path, dest_path)
                return True
            return False
        except Exception as msg:
            raise Exception(f"Error moving file: {msg}")
