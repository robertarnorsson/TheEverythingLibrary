import os
import shutil

class TELFileManager:
    def create_directory(self, dir: str) -> str:
        try:
            os.makedirs(dir, exist_ok=True)
            return dir
        except OSError as msg:
            raise OSError(f"Error creating directory: {msg}")
        except Exception as msg:
            raise Exception(f"Error deleting directory: {msg}")

    def delete_directory(self, dir: str) -> bool:
        try:
            if os.path.exists(dir) and os.path.isdir(dir):
                shutil.rmtree(dir)
                return True
            return False
        except Exception as msg:
            raise Exception(f"Error deleting directory: {msg}")

    def list_files(self, dir: str) -> list[str]:
        try:
            if os.path.exists(dir) and os.path.isdir(dir):
                files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
                return files
            return []
        except Exception as msg:
            raise Exception(f"Error listing files: {msg}")

    def copy_file(self, src_dir: str, src_file: str, dest_dir: str) -> bool:
        src_path = os.path.join(src_dir, src_file)
        dest_path = os.path.join(dest_dir, src_file)
        try:
            if os.path.exists(src_path) and os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)
                return True
            return False
        except Exception as msg:
            raise Exception(f"Error copying file: {msg}")

    def move_file(self, src_dir: str, src_file: str, dest_dir: str) -> bool:
        src_path = os.path.join(src_dir, src_file)
        dest_path = os.path.join(dest_dir, src_file)
        try:
            if os.path.exists(src_path) and os.path.isfile(src_path):
                shutil.move(src_path, dest_path)
                return True
            return False
        except Exception as msg:
            raise Exception(f"Error moving file: {msg}")
