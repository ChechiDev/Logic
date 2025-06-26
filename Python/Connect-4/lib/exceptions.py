

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
            message="Invalid name..."):

        super().__init__(message)