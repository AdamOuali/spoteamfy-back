import requests
import base64
import json
import logging
from getNewToken import getNewToken

token = getNewToken()


def getFavoriteTracks(limit=50, offset=0):
    tracks = []
    try:
        token_headers = {"Authorization": f"Bearer {token}"}
        token_url = (
            f"https://api.spotify.com/v1/me/tracks?limit={limit}&offset={offset}"
        )
        token_response = requests.get(token_url, headers=token_headers)
        token_response.raise_for_status()
        token_response = token_response.json()
        total_tracks = token_response["total"]
        tracks += token_response["items"]

        while len(tracks) < total_tracks:
            logging.info(f"Getting current tracks: {len(tracks)} / {total_tracks}")
            offset += limit
            token_url = (
                f"https://api.spotify.com/v1/me/tracks?limit={limit}&offset={offset}"
            )
            token_response = requests.get(token_url, headers=token_headers)
            token_response.raise_for_status()
            token_response = token_response.json()
            tracks += token_response["items"]

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return 0

    return tracks
