import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id="778c83d63af643e5b0f6b0709138d46a", client_secret="55dc766368994b83a5fa327149634194")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)



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
    for i in range(0,10000,100):
        for track in sp.playlist_tracks(playlist_URI,offset=i)["items"]:
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
    playlist_link = "https://open.spotify.com/playlist/5b8LndFlpCN5vLg5mTQWl4?si=42f039444ca74342"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    for i in range(0,10000,100):
        if len([x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI,offset=i)["items"]]) == 0:
            break
        get_audio_ftrs([x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI,offset=i)["items"]])
    get_songs()
    get_csv()