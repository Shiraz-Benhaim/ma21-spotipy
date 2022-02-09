"""Extract exceptions"""


class PathNotExist(Exception):
    pass


class FailedToParseJsonFile(Exception):
    pass


class KeyDoesNotExist(Exception):
    pass


"""Users"""


class UserDoesNotExist(Exception):
    pass


class UserAlreadyExist(Exception):
    pass


class WrongPassword(Exception):
    pass
