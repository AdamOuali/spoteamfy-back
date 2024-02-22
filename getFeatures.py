import json
import requests
from collections import Counter
from getFavoriteTracks import getFavoriteTracks
import logging


def getAllTracksIDs(token):
    favorite_tracks = getFavoriteTracks(token)
    tracks = []
    for track in favorite_tracks:
        currentID = track["track"]["id"]
        tracks.append(currentID)
    return tracks


def getFeatures(token):
    tracksIDs = getAllTracksIDs(token)
    headers = {"Authorization": f"{token}"}
    allFeatures = []

    try:
        for i in range(0, len(tracksIDs), 50):
            features = requests.get(
                f"https://api.spotify.com/v1/audio-features?ids={','.join(tracksIDs[i:i+50])}",
                headers=headers,
            ).json()
            for feature in features["audio_features"]:
                allFeatures.append(feature)

        return allFeatures

    except Exception as e:
        logging.error("An error occurred while getting features", exc_info=True)
        return {"error": "An error occurred"}
