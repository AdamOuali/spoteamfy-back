from flask import Flask
from flask import jsonify

from getFavoriteTracks import getFavoriteTracks
from getTopArtists import getTopArtists
from getTopGenres import getTopGenres
from flask import request

app = Flask(__name__)


@app.route("/favorite-tracks")
def favorite_tracks():
    tracks = getFavoriteTracks()
    return jsonify(tracks)


@app.route("/top-artists/<int:num_artists>")
def top_artists(num_artists=None):
    if num_artists is None:
        artists = getTopArtists()
    else:
        artists = getTopArtists(num_artists)
    return jsonify(artists)


@app.route("/top-genres")
def top_genres():
    genres = getTopGenres()
    return jsonify(genres)


@app.route("/cluster-genres")
def cluster_genres():
    return "<p> TODO w/ AI </p>"


# to run : python3 -m flask --app main run
