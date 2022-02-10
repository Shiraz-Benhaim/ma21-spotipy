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


class PlaylistAlreadyExist(Exception):
    pass


class UnauthorizedRequest(Exception):
    pass


"""Search"""


class ArtistIdNotFound(Exception):
    pass


class AlbumIdNotFound(Exception):
    pass


class ArtistIdNotFound(Exception):
    pass
