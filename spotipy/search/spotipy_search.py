import spotipy
from spotipy import ArtistIdNotFound, ArtistNameNotFound, ArtistFileKeys


class Search:
    def __init__(self):
        pass

    @staticmethod
    def get_all_tracks_ids():
        tracks = []
        for artist in spotipy.info.artists.keys():
            for album in spotipy.info.artists[artist].albums.keys():
                tracks += [track for track in spotipy.info.artists[artist].albums[album].songs.keys()]
        return tracks

    @staticmethod
    def artist_id_by_name(artist_name):
        try:
            for artist_id in spotipy.info.artists.keys():
                if spotipy.info.artists.get(artist_id).name == artist_name:
                    return artist_id
        except KeyError as e:
            raise ArtistNameNotFound(str(e))

    @staticmethod
    def albums_info_of_artist(artist_id):
        try:
            return [{ArtistFileKeys.ALBUM_ID_NAME: album_id,
                     ArtistFileKeys.ALBUM_NAME_NAME: spotipy.info.artists[artist_id].albums[album_id].name}
                    for album_id in spotipy.info.artists[artist_id].albums.keys()]
        except KeyError as e:
            raise ArtistIdNotFound(str(e))
