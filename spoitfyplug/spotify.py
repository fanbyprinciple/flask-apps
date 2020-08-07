import config

#print(config.config["client_id"])

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

client_credentials_manager = SpotifyClientCredentials(config.config["client_id"], config.config["client_secret"])
sp = spotipy.Spotify(client_credentials_manager)

def getTrackIds(user ,playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for itemin playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs('angelicadietzel', '4R0BZVh27NUJhHGLNitU08')

def getTrackFeatures(id):
    meta = sp.track(id)
    features=sp.audio_features(id)

    #meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity =meta['popularity']

    #features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']

    track = [name, album, artist, release_date, length, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature ]
    return track