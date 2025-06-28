from time import sleep
from lib import utils
from lib.exceptions import ExceptionBase, NameValidationError
from user import User


class Menu:
    def __init__(self):
        self._pattern = "="
        self._width = 80
        self._header_text = "CONNECT-4: The ultimate game"

        # Instancia a UTILS:
        self.ut = utils.Utils()


    def separator(self):
        """ Shows separation barr """

        print(self._pattern * self._width)

    def header(self):
        """ Shows the menu header """

        self.ut.clear_terminal()
        self.separator()
        print(self.ut.center_txt(self._header_text, self._width))
        self.separator()

    def footer(self):
        """ Show the footer of the menu """

        print("\n" * 4)
        self.separator()


class LandingMenu(Menu):
    def __init__(self):
        super().__init__()

        self._menu_opt = [
            "Register",
            # "Sign in",
            # "Game Rules",
            # "Statistics",
            # "Settings"
        ]

    def show_options(self):
        """ Display menu options """

        self.header()
        for idx, opt in enumerate(self._menu_opt):
            print(f"{idx + 1}. {opt}")

        print("\n0. Exit")
        self.footer()


class ExitMenu(Menu):
    def __init__(self):
        super().__init__()

    def exit(self):
        txt = "Exiting game in"
        count = 3

        for i in range(count, 0, -1):
            self.ut.clear_terminal()
            self.header()
            print(f"{txt} {i}...")  # Muestra mensaje con la cuenta atrás
            self.footer()
            sleep(1)

        self.ut.clear_terminal()
        self.header()
        print(f"Thank you for playing CONNECT-4!")
        self.footer()


class RegistrationMenu(Menu):
    def __init__(self):
        super().__init__()
        self._header_text = "User Registration"
        self._current_name = None

    def registration(self):
        """ Call to registration process """

        user = User(name=None)
        while True:
            self.ut.clear_terminal()
            self.header()

            if self._current_name:
                print(f"Name: {self._current_name}\n")

            else:
                print("Name: \n")

            try:
                self.footer()
                name = input("Enter your name: ")
                user.name = name
                self._current_name = user.name

                # Si todo OK, guardamos JSON
                user.dict_builder.send_to_json()
                sleep(1)
                break

            except NameValidationError as e:
                print(e)
                sleep(1)