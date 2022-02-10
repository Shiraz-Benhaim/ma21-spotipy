import spotipy
from spotipy import ArtistIdNotFound, AlbumIdNotFound
from spotipy.users.user import User


class SearchForUser:
    def __init__(self, user: User):
        self.user = user

    def get_artists_names(self):
        return [spotipy.info.artists[artist_id].name for artist_id in spotipy.info.artists.keys()]

    def albums_of_artist(self, artist_id):
        try:
            return [spotipy.info.artists[artist_id].albums[album_id].name
                    for album_id in spotipy.info.artists[artist_id].albums.keys()]
        except KeyError as e:
            raise ArtistIdNotFound(str(e))

    def sorted_ten_tracks_by_popularity_of_artist(self, artist_id):
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

    def tracks_of_album(self, album_id):
        try:
            for artist_id in spotipy.info.artists.keys():
                if album_id in [album for album in spotipy.info.artists[artist_id].albums.keys()]:
                    return [track_info.name for track_info in
                            spotipy.info.artists[artist_id].albums[album_id].songs.values()]
        except KeyError as e:
            raise AlbumIdNotFound(str(e))

