import spotipy
from spotipy import Search, ArtistFileKeys
from spotipy.users.user import User


def create_user(username, password, user_type):
    user_types = [RegularUser, PremiumUser, ArtistUser]
    return (user_types[user_type])(username, password)


class RegularUser(User):
    def __init__(self, username, password):
        super().__init__(username, password, False)


class PremiumUser(User):
    def __init__(self, username, password):
        super().__init__(username, password, True)


class ArtistUser(User):
    def __init__(self, username, password):
        super().__init__(username, password, True)

        self.albums = Search.albums_of_artist(Search.artist_id_by_name(username))
        self._user_data[ArtistFileKeys.ALBUMS_LIST_KEY_NAME] = \
            Search.albums_info_of_artist(Search.artist_id_by_name(username))
        self._update_user_file()

