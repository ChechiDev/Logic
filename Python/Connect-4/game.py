from time import sleep
from menu import LandingMenu, ExitMenu

def main():
    """ Main function: Manages the logic and organization of the Connect-4 game """
    menu = LandingMenu()
    ex_menu = ExitMenu()

    while True:
        menu.header()
        menu.show_options()

        try:
            opt = int(input("Please select an option: "))
            if opt == 0:
                ex_menu.exit()
                break

            else:
                print("Select an option: ")

        except ValueError:
            print("Please enter a valid option")


if __name__ == "__main__":
    main()