from lib import utils

class Menu:
    def __init__(self):
        self._pattern = "="
        self._width = 60
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

        print("\n" * 2)
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
        self.header()
        print("Exiting the game.\nSee you soon\nGoodbye!")
        self.footer()


if __name__ == "__main__":

    menu = LandingMenu()
    menu.header()
    menu.show_options()
