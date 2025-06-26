from lib.validation import Validation
from lib.exceptions import NameValidationError
from lib.utils import Utils
from time import sleep


class User:
    def __init__(self, name):
        self.name = name # Usamos el 'setter' para aplicar validación

    @property
    def name(self) -> str:
        """ Returns the str of the name """

        return self._name

    @name.setter
    def name(self, value: str):

        if Validation.val_string_length(value, min_length=3, max_length=15):
            self._name = value.capitalize()

        else:
            raise NameValidationError() # Usamos la excepción personalizada

        sleep(0.5)


if __name__ == "__main__":
    try:
        user = User(input("Write your name: "))
        print(user.name)


    except NameValidationError as e:
        print(e)