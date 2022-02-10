import json
from typing import List

import spotipy
from spotipy import Path, Suffix, UserFileKeys, PlaylistAlreadyExist, KeyDoesNotExist, utils, \
    UserPermissions, UnauthorizedRequest, Search
from spotipy.extract.extract_json import Json


class User:
    def __init__(self, username, password, is_premium):
        self.username = username
        self.password = password
        self._user_file_path = f"{Path.USERS_DIR}\\{username}{Suffix.JSON}"
        self._user_data = Json(self._user_file_path).data
        self._permissions = UserPermissions(is_premium)

    def _update_user_file(self):
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

    def __get_valid_tracks(self, songs):
        all_tracks_ids = Search.get_all_tracks_ids()
        return set(all_tracks_ids).intersection(songs)

    def __add_playlist_force(self, playlist_name, songs):
        songs_limit = self._permissions.PLAYLIST_TRACKS_NUM_LIMIT
        songs = songs if songs_limit is None or songs_limit >= len(songs) \
            else songs[:songs_limit]
        new_playlist = {UserFileKeys.PLAYLIST_NAME_KEY: playlist_name,
                        UserFileKeys.TRACKS_LIST_KEY_NAME: songs}
        self._user_data[UserFileKeys.PLAYLIST_LIST_KEY_NAME] = \
            self._user_data.get(UserFileKeys.PLAYLIST_LIST_KEY_NAME, []) + [new_playlist]
        self.__update_user_file()
        spotipy.log.info(f"Playlist '{playlist_name}' created successfully for user '{self.username}'")

    def add_playlist(self, playlist_name, songs: List[str]):
        spotipy.log.debug(f"User '{self.username}' tries to add playlist '{playlist_name}'")
        self.__playlist_name_validation(playlist_name)
        songs = list(self.__get_valid_tracks(songs))

        try:
            playlist_limit = self._permissions.PLAYLISTS_NUM_LIMIT
            if playlist_limit is None or len(self.__get_playlists_names()) < playlist_limit:
                self.__add_playlist_force(playlist_name, songs)
            else:
                spotipy.log.info(f"Playlist '{playlist_name}' did not created because there are already "
                                 f"{self._permissions.PLAYLISTS_NUM_LIMIT} playlists")
                raise UnauthorizedRequest(f"User '{self.username}' can not have more than "
                                          f"{self._permissions.PLAYLISTS_NUM_LIMIT} playlists")
        except AttributeError or TypeError as e:
            raise KeyDoesNotExist(e)
