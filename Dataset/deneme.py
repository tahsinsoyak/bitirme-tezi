import spotipy
import pandas as pd
import json
from spotipy.oauth2 import SpotifyClientCredentials




id = []
uri = []
song_name = []
artist_name = []
key = []
mode = []
danceability = []
energy = []
loudness = []
acousticness = []
speechiness = []
instrumentalness = []
liveness = []
tempo = []
valence = []
duration_ms = []
time_signature = []
popularity = []


def get_audio_ftrs(track_ur):
    datas = sp.audio_features(track_ur)
    for son in datas:
        id.append(son['id'])
        uri.append(son['uri'])
        key.append(son['key'])
        mode.append(son['mode'])
        danceability.append(son['danceability'])
        energy.append(son['energy'])
        loudness.append(son['loudness'])
        acousticness.append(son['acousticness'])
        speechiness.append(son['speechiness'])
        instrumentalness.append(son['instrumentalness'])
        liveness.append(son['liveness'])
        tempo.append(son['tempo'])
        valence.append(son['valence'])
        duration_ms.append(son['duration_ms'])
        time_signature.append(son['time_signature'])


    
def get_songs():
    for x in range(0,50):
        for track in sp.playlist_tracks(playlistids[x])["items"]:
            song_name.append(track["track"]["name"])
            popularity.append(track["track"]["popularity"])
            artist_name.append(track["track"]["artists"][0]["name"])




def get_csv():
    df = pd.DataFrame({'id': id,
                        'uri': uri,
                        'song_name':song_name,
                        'artist_name':artist_name,
                        'key': key,
                        'mode': mode,
                        'danceability': danceability,
                        'energy': energy,
                        'loudness': loudness,
                        'acousticness': acousticness,
                        'speechiness': speechiness,
                        'instrumentalness': instrumentalness,
                        'liveness': liveness,
                        'tempo': tempo,
                        'valence': valence,
                        'duration_ms': duration_ms,
                        'time_signature': time_signature,
                        'popularity':popularity
                        })

    df.to_csv('out.csv')




if __name__ == "__main__":
    spotifyid = "spotify"
    playlistids = []
    for i in range(0,500,100):
        deneme = sp.user_playlists(user=spotifyid,offset=i)["items"]
        for i in deneme:
            playlistids.append(i["uri"].split(":")[-1].split("?")[0])

    dt = pd.DataFrame({'id':playlistids})
    dt.to_csv('playlistids.csv')
    for x in range(0,50):
     get_audio_ftrs([x["track"]["uri"] for x in sp.playlist_tracks(playlistids[x])["items"]])
    get_songs()
    get_csv()







