from consolemenu import *
from consolemenu.items import *

import spotipy
from menu.menu_actions import Actions


def show_menu():
    menu = ConsoleMenu("Spotipy", f"Hello {spotipy.curr_user}!")
    playlist_creation = FunctionItem("Add playlist", Actions.add_playlist)

    search_options = SelectionMenu(["Artists names", "Albums of artist",
                                    "Top 10 tracks of artist", "Tracks of album"])
    search = SubmenuItem("Search", search_options, menu)

    menu.append_item(playlist_creation)
    menu.append_item(search)
    menu.show()


def run_spotipy():
    Actions.login_spotipy()

    if spotipy.curr_user is not None:
        show_menu()
