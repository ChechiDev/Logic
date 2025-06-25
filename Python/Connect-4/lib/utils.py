import os
import sys
import platform as plat

class Utils:

    @staticmethod
    def clear_terminal():
        """
        Clears the terminal screen based on the user's operating system.
        """
        if plat.system() == "Windows":
            os.system("cls")

        else:
            os.system("clear")

    @staticmethod
    def center_txt(txt: str, width: int) -> str:
        """
        Centers the given text within the specified width.

        Args:
            txt (str): The text to be centered.
            width (int): The total width within which the text will be centered.

        Returns:
            str: The centered text.
        """
        return txt.center(width)