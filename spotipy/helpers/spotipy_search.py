import spotipy
from spotipy import ArtistIdNotFound, AlbumIdNotFound, ArtistNameNotFound, ArtistFileKeys


class Search:
    def __init__(self):
        pass
    
    @staticmethod
    def get_artists_names():
        return [spotipy.info.artists[artist_id].name for artist_id in spotipy.info.artists.keys()]

    @staticmethod
    def albums_of_artist(artist_id):
        try:
            return [spotipy.info.artists[artist_id].albums[album_id].name
                    for album_id in spotipy.info.artists[artist_id].albums.keys()]
        except KeyError as e:
            raise ArtistIdNotFound(str(e))

    @staticmethod
    def sorted_ten_tracks_by_popularity_of_artist(artist_id):
        LIMIT = 10
        tracks = []

        try:
            for album_id in [album for album in spotipy.info.artists[artist_id].albums.keys()]:
                tracks += spotipy.info.artists[artist_id].albums[album_id].songs.values()

            sorted_tracks = [track_info.name for track_info in
                             sorted(tracks, key=lambda track: track.popularity, reverse=True)]
            return sorted_tracks if LIMIT >= len(sorted_tracks) else sorted_tracks[:LIMIT]
        except KeyError as e:
            raise ArtistIdNotFound(str(e))

    @staticmethod
    def tracks_of_album(album_id):
        try:
            for artist_id in spotipy.info.artists.keys():
                if album_id in [album for album in spotipy.info.artists[artist_id].albums.keys()]:
                    return [track_info.name for track_info in
                            spotipy.info.artists[artist_id].albums[album_id].songs.values()]
        except KeyError as e:
            raise AlbumIdNotFound(str(e))

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
