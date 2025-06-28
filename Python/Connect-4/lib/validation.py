import os
import sys
import re


class Validation:
    def __init__(self):
        pass

    @staticmethod
    def val_string_length(value: str, min_length: int, max_length: int) -> bool:
        # Acepta un rango min y max de carácteres
        pattern = rf"^.{{{min_length},{max_length}}}$"
        value = value.strip()

        return re.match(pattern, value) is not None

    @staticmethod
    def val_string(value: str) -> bool:
        # Acepta letras y espacios
        pattern = r"^[a-zA-Z\s]+$"
        value = value.strip()

        return re.match(pattern, value) is not None

    @staticmethod
    def normalize_spaces(value: str) -> str:
        value = value.strip()

        return re.sub(r"\s+", " ", value) # Con sub igualamos a replace

    @staticmethod
    def val_dni(value: str) -> bool:
        pass

    @staticmethod
    def val_email(value: str) -> bool:
        pass

    @staticmethod
    def val_date(value: str) -> bool:
        pass

    @staticmethod
    def val_postal_code(value: str) -> bool:
        pass

    @staticmethod
    def val_phone(value: str) -> bool:
        pass