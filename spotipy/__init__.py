from spotipy.constants import *
from spotipy.exceptions import *
from spotipy.extract.json_to_obj import json_to_spotify_data
import spotipy.logger
from spotipy.helpers.spotipy_search import Search
from spotipy.search import SearchRequests
from spotipy.users import login
from spotipy.utils import *

# globals
log = spotipy.logger.create_logger()
info = json_to_spotify_data(Path.SONGS_DIR)
Utils.create_folder_if_not_exists(Path.USERS_DIR)
curr_user = None


def run():
    try:
        """
        search = SearchRequests(UserPermissions(False))

        print(search.search_any_request(Search.get_artists_names))
        print(search.search_any_request(Search.albums_of_artist, "2l6M7GaS9x3rZOX6nDX3CM"))
        print(search.search_any_request(Search.sorted_ten_tracks_by_popularity_of_artist, "39jFFncu6W0phhYK16Dp9g"))
        print(search.search_any_request(Search.tracks_of_album, "6RWrvfIB8WGLNwYN1SKvZA"))

        for artist in info.artists.keys():
            print("artist:", info.artists[artist].name)
            for album in info.artists[artist].albums.keys():
                print("album:", info.artists[artist].albums[album].name)
                for song in info.artists[artist].albums[album].songs.keys():
                    print("song:", info.artists[artist].albums[album].songs[song].name,
                          info.artists[artist].albums[album].songs[song].popularity)
            print()
            print()
        """
    except PathNotExist or FailedToParseJsonFile as e:
        print(e)

    try:
        user = login("Dua Lipa", "pass")
    except UserDoesNotExist as e:
        print(e)
        return

    try:
        user.add_playlist("play1", ["0xu3PasKYiRNedJOnRBkJA", "2l6M7GaS9x3rZOX6nDX3CM"])
        user.add_playlist("play2", ["1", "3", "4"])
        user.add_playlist("play2", ["1", "3", "4"])
    except PlaylistAlreadyExist as e:
        print(e)
    except KeyDoesNotExist as e:
        print(e)
