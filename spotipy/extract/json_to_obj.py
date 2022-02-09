import os

from spotipy.extract.extract_json import Json
from spotipy.module import Album, Track, Artist, SpotifyData
from spotipy.constants import SongFileKeys
from spotipy import PathNotExist
from spotipy import FailedToParseJsonFile
from spotipy import KeyDoesNotExist


def json_to_spotify_data(dir_path):
    info = SpotifyData()

    if not os.path.exists(dir_path):
        raise PathNotExist("Path " + dir_path + " not found")

    for roots, dirs, files in os.walk(dir_path):
        for file in files:
            try:
                add_data_of_json_file(info, dir_path + "//" + file)
            except KeyDoesNotExist as e:
                raise FailedToParseJsonFile("Cannot extract file " + file + ": " + str(e))

    return info


def add_data_of_json_file(info, path):
    try:
        json_data = Json(path).data.get(SongFileKeys.TRACK_KEY_NAME)
        for artist in json_data.get(SongFileKeys.ARTISTS_LIST_KEY_NAME):
            add_album_to_artist(info,
                                artist,
                                album_id=json_data.get(SongFileKeys.ALBUM_KEY_NAME).get(SongFileKeys.ALBUM_ID_NAME),
                                album=Album(json_data.get(SongFileKeys.ALBUM_KEY_NAME).get(SongFileKeys.ALBUM_NAME_NAME)),
                                track_id=json_data.get(SongFileKeys.TRACK_ID_NAME),
                                track=Track(json_data.get(SongFileKeys.TRACK_NAME_NAME),
                                            json_data.get(SongFileKeys.TRACK_POPULARITY_NAME)))
    except AttributeError or TypeError as e:
        raise KeyDoesNotExist(e)


def add_album_to_artist(info, artist, album_id, album, track_id, track):
    artist_id = artist.get(SongFileKeys.ARTIST_ID_NAME)
    artist_name = artist.get(SongFileKeys.ARTIST_NAME_NAME)

    info.artists[artist_id] = info.artists.get(artist_id, Artist(artist_name))
    info.artists[artist_id].albums[album_id] = \
        info.artists[artist_id].albums.get(album_id, album)
    info.artists[artist_id].albums[album_id].songs[track_id] = \
        info.artists[artist_id].albums[album_id].songs.get(track_id, track)
