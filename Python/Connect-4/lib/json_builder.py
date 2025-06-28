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

            return folder

        except Exception:
            raise JSONError()


    def build_json(self, data: dict):
        """ Saves the dictionary to a JSON file from dict_builder """
        try:
            self.check_folder() # Miramos si existe la carpeta

            # Leemos el contenido del archivo JSON, si existe:
            if os.path.exists(self._file_path):
                with open(self._file_path, "r", encoding="UTF-8") as json_file:
                    try:
                        file_data = json.load(json_file)

                    except json.JSONDecodeError:
                        file_data = {}

            else:
                file_data = {}

            # Actualizamos el contenido del JSON:
            if "users" not in file_data:
                file_data["users"] = []

            file_data["users"].append(data) # agregamos nuevo usuario

            # Guardamos el contenido actualizado en el JSON:
            with open(self._file_path, "w", encoding="UTF-8") as json_file:
                json.dump(file_data, json_file, indent=4)


        except Exception:
            raise JSONError()


    def load_json(self):
        pass