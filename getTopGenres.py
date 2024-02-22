import json
import requests
from collections import Counter
from getFavoriteTracks import getFavoriteTracks
import logging


def getArtistIDs(token):
    try:
        favorite_tracks = getFavoriteTracks(token)
        artist_ids = []
        for track in favorite_tracks:
            for artist in track["track"]["album"]["artists"]:
                artist_ids.append(artist["id"])

        return artist_ids
    except Exception as e:
        logging.error("An error occurred while getting artist IDs", exc_info=True)
        return {"error": "An error occurred"}


def getArtists(token, artist_ids):
    all_artists = []

    try:
        for i in range(0, len(artist_ids), 50):
            artists = requests.get(
                f"https://api.spotify.com/v1/artists?ids={','.join(artist_ids[i:i+50])}",
                headers={"Authorization": f"{token}"},
            ).json()

            packOf50Artists = artists["artists"]
            all_artists.append(packOf50Artists)
    except Exception as e:
        logging.error("An error occurred while getting artists", exc_info=True)
        return {"error": "An error occurred"}

    return all_artists


def getTopGenres(token, n=20):
    all_artists = getArtists(token, getArtistIDs(token))
    genres = []
    for artists in all_artists:
        for artist in artists:
            genres.append(artist["genres"])

    genres_count = Counter([genre for sublist in genres for genre in sublist])
    top_genres = genres_count.most_common(n)
    top_genres_json = [
        {
            "rank": index + 1,
            "title": genre[0],
            "value": genre[1],
        }
        for index, genre in enumerate(top_genres)
    ]

    logging.info("Successfully retrieved top genres")
    return top_genres_json
