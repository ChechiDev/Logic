import os
import json
from exceptions import JSONError

class JSONBuilder:
    def __init__(self, file_path: str):
        self._file_path = file_path


    def check_folder(self):
        """ Checks if the folder exists, creates it if not, and returns the folder path """
        folder = os.path.dirname(self._file_path)

        try:
            if folder and not os.path.exists(folder):
                os.makedirs(folder)
                print(f"Folder {folder} created")

            else:
                print(f"Folder {folder} already exists!")

            return folder

        except Exception as e:
            raise JSONError()


    def build_json(self):
        pass


    def load_json(self):
        pass


# Debbug:
if __name__ == "__main__":
    file_path = r"data\test.json"
    builder = JSONBuilder(file_path)

    builder.check_folder()