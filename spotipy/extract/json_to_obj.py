import os

from spotipy.extract.extract_json import Json
from spotipy.module import Album, Track, Artist, SpotifyData
from spotipy.constants import SongFileKeys


def json_to_spotify_data(dir_path):
    info = SpotifyData()

    for roots, dirs, files in os.walk(dir_path):
        for file in files:
            add_data_of_json_file(info, dir_path + "//" + file)

    return info


def add_data_of_json_file(info, path):
    json_data = Json(path).data.get(SongFileKeys.TRACK_KEY_NAME)

    for artist in json_data.get(SongFileKeys.ARTISTS_LIST_KEY_NAME):
        add_album_to_artist(info,
                            artist,
                            album_id=json_data.get(SongFileKeys.ALBUM_KEY_NAME).get(SongFileKeys.ALBUM_ID_NAME),
                            album=Album(json_data.get(SongFileKeys.ALBUM_KEY_NAME).get(SongFileKeys.ALBUM_NAME_NAME)),
                            track_id=json_data.get(SongFileKeys.TRACK_ID_NAME),
                            track=Track(json_data.get(SongFileKeys.TRACK_NAME_NAME),
                                        json_data.get(SongFileKeys.TRACK_POPULARITY_NAME)))


def add_album_to_artist(info, artist, album_id, album, track_id, track):
    artist_id = artist.get(SongFileKeys.ARTIST_ID_NAME)
    artist_name = artist.get(SongFileKeys.ARTIST_NAME_NAME)

    info.artists[artist_id] = info.artists.get(artist_id, Artist(artist_name))
    info.artists[artist_id].albums[album_id] = \
        info.artists[artist_id].albums.get(album_id, album)
    info.artists[artist_id].albums[album_id].songs[track_id] = \
        info.artists[artist_id].albums[album_id].songs.get(track_id, track)
