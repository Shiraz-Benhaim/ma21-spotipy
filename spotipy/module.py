from typing import List


class Song:
    def __init__(self, id, name, popularity, genre):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.genre = genre


class Album:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.songs = List[Song]


class Artist:
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.albums = List[Album]
        self.genre = genre
