from flask import Flask, render_template, request, redirect, url_for

import spotipy
from spotipy import SearchForUser, ArtistIdNotFound, AlbumIdNotFound

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return render_template("welcome.html")


@app.route('/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        spotipy.curr_user = spotipy.login(username, password)
        return redirect(url_for('search'))
    except Exception as e:
        return "User does not exist"


@app.route('/search', methods=['GET'])
def search():
    search_options = ["Artists_names", "Albums_of_artist", "Top_10_tracks_of_artist", "Tracks_of_album"]
    return render_template("search.html", options=search_options)


@app.route('/search/Artists_names', methods=['GET'])
def search_artists_names():
    try:
        results = spotipy.curr_user.search_any_request(SearchForUser(spotipy.curr_user).get_artists_names)
        return "<br>".join(results)
    except ArtistIdNotFound or AlbumIdNotFound as e:
        return "Invalid input: " + str(e)
    except Exception as e:
        return str(e)


@app.route('/search/Albums_of_artist', methods=['GET'])
def search_albums_of_artist():
    return render_template("search_parameter.html", param_name="artist id")


@app.route('/search/Albums_of_artist', methods=['POST'])
def show_albums_of_artist():
    try:
        param = request.form['param']
        results = spotipy.curr_user.search_any_request(SearchForUser(spotipy.curr_user).albums_of_artist, param)
        return "<br>".join(results)
    except ArtistIdNotFound or AlbumIdNotFound as e:
        return "Invalid input: " + str(e)
    except Exception as e:
        return str(e)


@app.route('/search/Top_10_tracks_of_artist', methods=['GET'])
def search_top_10_tracks_of_artist():
    return render_template("search_parameter.html", param_name="artist id")


@app.route('/search/Top_10_tracks_of_artist', methods=['POST'])
def show_top_10_tracks_of_artist():
    try:
        param = request.form['param']
        results = spotipy.curr_user.search_any_request(SearchForUser(spotipy.curr_user).sorted_ten_tracks_by_popularity_of_artist, param)
        return "<br>".join(results)
    except ArtistIdNotFound or AlbumIdNotFound as e:
        return "Invalid input: " + str(e)
    except Exception as e:
        return str(e)


@app.route('/search/Tracks_of_album', methods=['GET'])
def search_tracks_of_album():
    return render_template("search_parameter.html", param_name="album id")


@app.route('/search/Tracks_of_album', methods=['POST'])
def search_tracks_of_album():
    try:
        param = request.form['param']
        results = spotipy.curr_user.search_any_request(SearchForUser(spotipy.curr_user).tracks_of_album, param)
        return "<br>".join(results)
    except ArtistIdNotFound or AlbumIdNotFound as e:
        return "Invalid input: " + str(e)
    except Exception as e:
        return str(e)


def run():
    app.run(host='0.0.0.0', port=2345)
