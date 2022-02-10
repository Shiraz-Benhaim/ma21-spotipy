from consolemenu import *
from consolemenu.items import *

import spotipy
from menu.menu_actions import Actions
from spotipy import SearchForUser


def search_menu():
    menu = ConsoleMenu("Spotipy", f"Search menu", exit_option_text="Return to main menu")

    menu.append_item(FunctionItem("Artists names", Actions.search_in_spotipy,
                                  [SearchForUser(spotipy.curr_user).get_artists_names]))
    menu.append_item(FunctionItem("Albums of artist", Actions.search_in_spotipy,
                                  [SearchForUser(spotipy.curr_user).albums_of_artist, "artist id"]))
    menu.append_item(FunctionItem("Top 10 tracks of artist", Actions.search_in_spotipy,
                                  [SearchForUser(spotipy.curr_user).sorted_ten_tracks_by_popularity_of_artist,
                                   "artist id"]))
    menu.append_item(FunctionItem("Tracks of album", Actions.search_in_spotipy,
                                  [SearchForUser(spotipy.curr_user).tracks_of_album, "album id"]))

    menu.show()


def main_menu():
    menu = ConsoleMenu("Spotipy", f"Hello {spotipy.curr_user.username}!")

    playlist_creation = FunctionItem("Add playlist", Actions.add_playlist)
    search = FunctionItem("Search", search_menu)

    menu.append_item(playlist_creation)
    menu.append_item(search)

    menu.show()


def run_spotipy():
    Actions.login_spotipy()

    if spotipy.curr_user is not None:
        main_menu()

    print("Goodbye!")
