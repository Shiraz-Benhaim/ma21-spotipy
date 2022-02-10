import json
from typing import List

import spotipy
from spotipy import Path, Suffix, UserFileKeys, PlaylistAlreadyExist, KeyDoesNotExist, utils
from spotipy.extract.extract_json import Json


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._user_file_path = f"{Path.USERS_DIR}\\{username}{Suffix.JSON}"
        self._user_data = Json(self._user_file_path).data

    def __update_user_file(self):
        """Will be called after every change in data"""
        utils.Utils.write_to_file(self._user_file_path, json.dumps(self._user_data))

    def __get_playlists_names(self):
        try:
            playlists = self._user_data.get(UserFileKeys.PLAYLIST_LIST_KEY_NAME)
            return [playlist.get(UserFileKeys.PLAYLIST_NAME_KEY) for playlist in playlists]
        except AttributeError or TypeError as e:
            raise KeyDoesNotExist(e)

    def __playlist_name_validation(self, playlist_name):
        try:
            playlists_names = self.__get_playlists_names()
            if playlist_name in playlists_names:
                spotipy.log.info(f"Creation of playlist '{playlist_name}' failed because playlist already exist")
                raise PlaylistAlreadyExist(f"Playlist '{playlist_name}' already exist")
        except KeyDoesNotExist:
            spotipy.log.info(f"Creation of playlist '{playlist_name}' failed because the json file is in a bad format")

    def __add_playlist_force(self, playlist_name, songs):
        new_playlist = {UserFileKeys.PLAYLIST_NAME_KEY: playlist_name,
                        UserFileKeys.TRACKS_LIST_KEY_NAME: songs}
        self._user_data[UserFileKeys.PLAYLIST_LIST_KEY_NAME] = \
            self._user_data.get(UserFileKeys.PLAYLIST_LIST_KEY_NAME, []) + [new_playlist]
        self.__update_user_file()
        spotipy.log.info(f"Playlist '{playlist_name}' created successfully for user '{self.username}'")

    def add_playlist(self, playlist_name, songs: List[str]):
        spotipy.log.debug(f"User '{self.username}' tries to add playlist '{playlist_name}'")
        self.__playlist_name_validation(playlist_name)

        try:
            self.__add_playlist_force(playlist_name, songs)
        except AttributeError or TypeError as e:
            raise KeyDoesNotExist(e)
