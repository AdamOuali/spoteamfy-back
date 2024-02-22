import json
from collections import Counter
import logging
from getFavoriteTracks import getFavoriteTracks


def getTopArtists(token, n=20):
    try:
        favorite_tracks = getFavoriteTracks(token)
        artists = []
        for track in favorite_tracks:
            for artist in track["track"]["album"]["artists"]:
                artists.append(artist["name"])

        artist_counts = Counter(artists)
        top_artists = artist_counts.most_common(n)
        top_artists_json = [
            {
                "rank": index + 1,
                "name": artist[0],
                "count": artist[1],
            }
            for index, artist in enumerate(top_artists)
        ]

        return top_artists_json
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
