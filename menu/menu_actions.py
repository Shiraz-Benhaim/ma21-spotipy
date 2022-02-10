import spotipy
from spotipy import AlbumIdNotFound, ArtistIdNotFound


class Actions:
    @staticmethod
    def login_spotipy():
        username = input("Username: ")
        password = input("Password: ")
        try:
            spotipy.curr_user = spotipy.login(username, password)
            print(f"User {username} logged in")
        except Exception as e:
            print(e)

    @staticmethod
    def add_playlist():
        playlist_name = input("Enter name of the new playlist: ")
        tracks = []

        tracks += [input("Enter tracks ids (press twice on Enter to finish): ")]
        while True:
            track = input()
            if track == "":
                break
            else:
                tracks += [track]

        try:
            spotipy.curr_user.add_playlist(playlist_name, tracks)
            print(f"Playlist {playlist_name} added successfully")
        except Exception as e:
            print(e)

    @staticmethod
    def search_in_spotipy(func, *args):
        function_args = []
        for arg in args:
            function_args += [input(f"Enter {arg}")]

        try:
            result = spotipy.curr_user.search_any_request(func, *function_args)
            for r in result:
                print(r)
        except ArtistIdNotFound or AlbumIdNotFound as e:
            print("Invalid input: " + str(e))
        except Exception as e:
            print(e)