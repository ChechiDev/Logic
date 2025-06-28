import os
import json
from lib.exceptions import JSONError

class JSONBuilder:
    def __init__(self, file_path: str):
        self._file_path = os.path.abspath(file_path) # ruta absoluta


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

        except Exception:
            raise JSONError()


    def build_json(self, data: dict):
        """ Saves the dictionary to a JSON file from dict_builder """
        try:
            self.check_folder()
            with open(self._file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

        except Exception:
            raise JSONError()


    def load_json(self):
        pass


# Debbug:
if __name__ == "__main__":
    file_path = r"data\test.json"
    builder = JSONBuilder(file_path)

    builder.check_folder()