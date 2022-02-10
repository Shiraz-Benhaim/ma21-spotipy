from flask import Flask, render_template, request

import spotipy

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
        return f"hello {username}"
    except Exception as e:
        return "User does not exist"


def run():
    app.run(host='0.0.0.0', port=2345)
