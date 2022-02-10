import spotipy
from spotipy import ArtistIdNotFound, AlbumIdNotFound
from spotipy.module import SpotifyData


class SearchRequests:
    def __init__(self, data: SpotifyData):
        self.__data = data

    def get_artists_names(self):
        return [self.__data.artists[artist_id].name for artist_id in self.__data.artists.keys()]

    def albums_of_artist(self, artist_id):
        try:
            return [self.__data.artists[artist_id].albums[album_id].name
                    for album_id in self.__data.artists[artist_id].albums.keys()]
        except KeyError as e:
            raise ArtistIdNotFound(str(e))

    def sorted_ten_tracks_by_popularity_of_artist(self, artist_id):
        LIMIT = 10
        tracks = []

        try:
            for album_id in [album for album in self.__data.artists[artist_id].albums.keys()]:
                tracks += self.__data.artists[artist_id].albums[album_id].songs.values()

            sorted_tracks = [track_info.name for track_info in
                             sorted(tracks, key=lambda track: track.popularity, reverse=True)]
            return sorted_tracks if LIMIT >= len(sorted_tracks) else sorted_tracks[:LIMIT]
        except KeyError as e:
            raise ArtistIdNotFound(str(e))

    def tracks_of_album(self, album_id):
        try:
            for artist_id in self.__data.artists.keys():
                if album_id in [album for album in self.__data.artists[artist_id].albums.keys()]:
                    return [track_info.name for track_info in
                            self.__data.artists[artist_id].albums[album_id].songs.values()]
        except KeyError as e:
            raise AlbumIdNotFound(str(e))

    def search_any_request(self, func, *args):
        def inner():
            return func(*args)

        try:
            result = inner()
            return result
        except Exception as e:
            spotipy.log.info(f"Search failed because of bad input to search")
            raise e
