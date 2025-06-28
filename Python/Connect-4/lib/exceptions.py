

class ExceptionBase(Exception):
    """ Base class for all custom exceptions """
    def __init__(self, message):
        self._message = message

    def __str__(self):
        """ Returns the exception message as a string """
        return self._message


class NameValidationError(ExceptionBase):
    def __init__(
            self,
            message=f"\033[91mError: Invalid name...\033[0m"
            ):

        super().__init__(message)


class JSONError(ExceptionBase):
    def __init__(
            self,
            message=f"\033[91mError: Error processing JSON file...\033[0m"
            ):

        super().__init__(message)