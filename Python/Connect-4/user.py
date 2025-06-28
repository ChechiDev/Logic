from lib.validation import Validation
from lib.exceptions import NameValidationError
from lib.utils import Utils
from lib.dict_builder import DictBuilder

from time import sleep


class User:
    def __init__(self, name):
        # Enviamos los attr a la instancia de dict_builder:
        self.dict_builder = DictBuilder()

        self.name = name # Usamos el 'setter' para aplicar validación


    @property
    def name(self) -> str:
        """ Returns the str of the name """

        return self._name

    @name.setter
    def name(self, value: str):
        # Normalizamos los espacios:
        value = Validation.normalize_spaces(value)

        # Validación: Longitud mínima de texto:
        if not Validation.val_string_length(value, min_length=3, max_length=25):
            min_length = min_length
            max_length = max_length
            raise NameValidationError(
                f"\033[91mError: Name -> '{value}' must be between {min_length} and {max_length} characters.\033[0m"
                )

        # Validación: Que el nombre no contenga números:
        if not Validation.val_string(value):
            raise NameValidationError(
                f"\033[91mError: Name -> '{value}' must contain only alphabetic characters without accents.\033[0m"
                )

        self._name = value.title()

        # Enviamos el attr a dict_builder:
        self.dict_builder.add_attr("name", self._name)


if __name__ == "__main__":
    try:
        user = User(input("Write your name: "))
        print(user.name) # Imprimimos el atributo directamente del decorator @property

        # Imprimimos el dict generado:
        print(user.dict_builder.get_dict())

    except NameValidationError as e:
        print(e) # Mostramos el mensaje específico para cada validación