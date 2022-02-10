import json
import os

import spotipy
from spotipy import Path, Suffix, UserFileKeys, UserTypes, utils, UserDoesNotExist
from spotipy.extract.extract_json import Json
from spotipy.users.different_users import create_user


def login(username, password):
    spotipy.log.debug(f"Attempt to login with username '{username}' and password '{password}'")
    user_file_path = f"{Path.USERS_DIR}\\{username}{Suffix.JSON}"
    if os.path.exists(user_file_path):
        try:
            user_data = Json(user_file_path).data
            user = create_user(username, password, user_data.get(UserFileKeys.USER_TYPE_KEY_NAME, UserTypes.REGULAR))
            spotipy.log.info(f"User '{username}' logged in successfully")
            return user
        except Exception as e:
            spotipy.log.info(f"Login attempt failed because file '{username}' is in bad format")
            raise e
    else:
        """ DEBUG"""
        user_type = 0  # TODO: check if username is in artists
        user_file = {UserFileKeys.PASSWORD_KEY_NAME: password,
                     UserFileKeys.USER_TYPE_KEY_NAME: 0,
                     UserFileKeys.PLAYLIST_LIST_KEY_NAME: []}
        utils.Utils.write_to_file(f"{Path.USERS_DIR}\\{username}{Suffix.JSON}", json.dumps(user_file))

        spotipy.log.info(f"Login attempt failed because the user '{username}' does not exist")
        raise UserDoesNotExist(f"User '{username}' does not exist")
