from spotipy.users.user import User


def create_user(username, password, user_type, *args):
    user_types = [RegularUser, PremiumUser, ArtistUser]
    return (user_types[user_type])(username, password, *args)


class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password, False)


class PremiumUser(User):
    def __init__(self, username, password):
        super().__init__(username, password, True)


class ArtistUser(User):
    def __init__(self, username, password, albums={}):
        super().__init__(username, password, True)
        self.albums = albums
