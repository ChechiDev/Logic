from lib import utils


class Board:
    def __init__(self):
        self.utils = utils.Utils() # Instancia a utils

        self.utils.clear_terminal()


if __name__ == "__main__":
    board = Board()