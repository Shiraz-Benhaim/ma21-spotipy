import os

from spotipy.exceptions import *
from spotipy.extract.json_to_obj import json_to_spotify_data
import spotipy.logger

log = spotipy.logger.create_logger()


def run():
    try:
        info = json_to_spotify_data(os.path.abspath("songs"))
        for artist in info.artists.keys():
            print("artist:", info.artists[artist].name)
            for album in info.artists[artist].albums.keys():
                print("album:", info.artists[artist].albums[album].name)
                for song in info.artists[artist].albums[album].songs.keys():
                    print("song:", info.artists[artist].albums[album].songs[song].name,
                          info.artists[artist].albums[album].songs[song].popularity)
            print()
            print()
    except exceptions.FailedToParseJsonFile as e:
        print(e)
