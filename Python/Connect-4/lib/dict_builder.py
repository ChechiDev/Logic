from lib.json_builder import JSONBuilder

class DictBuilder:
    def __init__(self):
        self._user_dict = {}


    def add_attr(self, k, v):
        """ Adds an attr. to the dict """
        self._user_dict[k] = v


    def get_dict(self):
        """ Return the dict builded """

        return self._user_dict

    def send_to_json(self):
        """ Send the build dict to JSONBuilder """
        file_path = r"data\test.json"
        json_builder = JSONBuilder(file_path)

        json_builder.build_json(self._user_dict)