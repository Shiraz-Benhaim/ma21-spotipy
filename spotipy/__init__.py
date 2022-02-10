from spotipy.constants import *
from spotipy.exceptions import *
import spotipy.logger
from spotipy.search import SearchForUser
from spotipy.users import login

# globals
from spotipy.users.user import User

log = spotipy.logger.create_logger()
info = spotipy.extract.json_to_obj.json_to_spotify_data(Path.SONGS_DIR)
spotipy.utils.Utils.create_folder_if_not_exists(Path.USERS_DIR)
curr_user = None


def run():
    try:
        u = User("lili", "pass", False)
        search = SearchForUser(u)

        print(u.search_any_request(search.get_artists_names))
        print(u.search_any_request(search.albums_of_artist, "2l6M7GaS9x3rZOX6nDX3CM"))
        print(u.search_any_request(search.sorted_ten_tracks_by_popularity_of_artist, "39jFFncu6W0phhYK16Dp9g"))
        print(u.search_any_request(search.tracks_of_album, "6RWrvfIB8WGLNwYN1SKvZA"))

        """
        for artist in info.artists.keys():
            print("artist:", info.artists[artist].name)
            for album in info.artists[artist].albums.keys():
                print("album:", info.artists[artist].albums[album].name)
                for song in info.artists[artist].albums[album].songs.keys():
                    print("song:", info.artists[artist].albums[album].songs[song].name,
                          info.artists[artist].albums[album].songs[song].popularity)
            print()
            print()"""
    except PathNotExist or FailedToParseJsonFile as e:
        print(e)
