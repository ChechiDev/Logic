import os
import sys
import re


class Validation:
    def __init__(self):
        pass

    @staticmethod
    def val_string_length(value: str, min_length: int, max_length: int) -> bool:
        pattern = rf"^.{{{min_length},{max_length}}}$"
        value = value.strip().capitalize()

        return re.match(pattern, value) is not None

    @staticmethod
    def val_string(value: str) -> bool:
        pass

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