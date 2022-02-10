import os


class Path:
    SONGS_DIR = os.path.abspath("songs\\")
    USERS_DIR = os.path.abspath("users\\")
    SPOTIPY_INFO = os.path.abspath("info.p")


class Suffix:
    JSON = ".json"


class SongFileKeys:
    TRACK_KEY_NAME = "track"
    ALBUM_KEY_NAME = "album"
    ARTISTS_LIST_KEY_NAME = "artists"

    TRACK_ID_NAME = ALBUM_ID_NAME = ARTIST_ID_NAME = "id"
    TRACK_NAME_NAME = ALBUM_NAME_NAME = ARTIST_NAME_NAME = "name"
    TRACK_POPULARITY_NAME = "popularity"


class UserFileKeys:
    PASSWORD_KEY_NAME = "password"
    PLAYLIST_LIST_KEY_NAME = "playlists"
    PLAYLIST_NAME_KEY = "name"
    TRACKS_LIST_KEY_NAME = "tracks"
