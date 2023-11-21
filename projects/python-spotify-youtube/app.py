import pyyoutube
import os
import json
from flask import Flask, request


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ["SPOTIPY_CLIENT_ID"] = "CLIENT_ID"
os.environ["SPOTIPY_CLIENT_SECRET"]="CLIENT_SECRET"


app = Flask(__name__)

@app.route('/artistalbums', methods=['GET'])
def getalbums():
    albumname = []
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])
        albumname.append(album['name'])
    return albumname


getalbums()

if __name__ == "__main__":
    app.run(debug=True, port=3000)
