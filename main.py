from flask import Flask
from flask import jsonify
from flask_cors import CORS

from getFavoriteTracks import getFavoriteTracks
from getTopArtists import getTopArtists
from getTopGenres import getTopGenres
from getFeatures import getFeatures
from getClusterGraph import getClusterGraph
from flask import request
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)


def getTokenViaHeader(request):
    logging.info(request.headers.get("Authorization"))
    return request.headers.get("Authorization")  # already contains "Bearer"


@app.route("/favorite-tracks")
def favorite_tracks():
    token = getTokenViaHeader(request)
    if token is None:
        return jsonify({"error": "No token provided"}), 400
    else:
        tracks = getFavoriteTracks(token)
    return jsonify(tracks)


@app.route("/top-artists/<int:num_artists>")
def top_artists(num_artists=None):
    token = getTokenViaHeader(request)
    if token is None:
        return jsonify({"error": "No token provided"}), 400
    else:
        artists = getTopArtists(token, num_artists)
    return jsonify(artists)


@app.route("/top-genres")
def top_genres():
    token = getTokenViaHeader(request)
    if token is None:
        return jsonify({"error": "No token provided"}), 400
    else:
        genres = getTopGenres(token)
    return jsonify(genres)


@app.route("/cluster-features")
def cluster_genres():
    token = getTokenViaHeader(request)
    if token is None:
        return jsonify({"error": "No token provided"}), 400
    else:
        features = getFeatures(token)
    return jsonify(features)


@app.route("/cluster-graph")
def cluster_graph():
    token = getTokenViaHeader(request)
    if token is None:
        return jsonify({"error": "No token provided"}), 400
    else:
        clusterGraph = getClusterGraph(token)
    return clusterGraph


# to run : python3 -m flask --app main run
