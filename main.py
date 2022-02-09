from spotipy import Json


def main():
    x = Json("songs//song_2fuCquhmrzHpu5xcA1ci9x.json")
    print(x.data)
    print(x.data.get("track"))
    print(x.data.get("track").get("album"))


if __name__ == '__main__':
    main()
