import os
import json
# from lib.exceptions import ExceptionBase

class JSONBuilder:
    def __init__(self, file_path: str):
        self._file_path = file_path


    def check_folder(self):
        folder = os.path.dirname(self._file_path)

        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder {folder} created")

        else:
            print(f"Folder {folder} already exists!")

        return folder


    def build_json(self):
        pass


    def load_json(self):
        pass


if __name__ == "__main__":
    file_path = r"data\test.json"
    builder = JSONBuilder(file_path)

    builder.check_folder()