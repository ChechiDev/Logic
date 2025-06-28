import json


class DictBuilder:
    def __init__(self):
        self._user_dict = {}


    def add_attr(self, k, v):
        """ Adds an attr. to the dict """
        self._user_dict[k] = v


    def get_dict(self):
        """ Return the dict builded """

        return self._user_dict


if __name__ == "__main__":
    pass