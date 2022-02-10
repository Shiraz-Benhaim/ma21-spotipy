class Track:
    def __init__(self, name, popularity):
        self.name = name
        self.popularity = popularity


class Album:
    def __init__(self, name):
        self.name = name
        self.songs = {}


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = {}


class SpotifyData:
    def __init__(self):
        self.artists = {}
