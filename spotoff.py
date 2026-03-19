import csv
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-read-private playlist-read-collaborative"
))

playlists = []
response = sp.current_user_playlists()
while response:
    playlists.extend(response["items"])
    response = sp.next(response) if response["next"] else None

writer = csv.writer(sys.stdout)
writer.writerow(["playlist", "track", "artist", "album"])

for playlist in playlists:
    tracks = []
    response = sp.playlist_items(playlist["id"], fields="items(track(name,artists(name),album(name))),next")
    while response:
        tracks.extend(response["items"])
        response = sp.next(response) if response["next"] else None

    for item in tracks:
        track = item["track"]
        if not track:
            continue
        writer.writerow([
            playlist["name"],
            track["name"],
            ", ".join(a["name"] for a in track["artists"]),
            track["album"]["name"],
        ])
