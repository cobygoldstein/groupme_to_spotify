from Groupy.groupy.client import Client
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

#Groupme Credentials
token = "6eea8e90655201381f9e3e0b29adb3a5"
client = Client.from_token(token)
# Searches a groupme group for spotify links
# returns a list of track ID's
def get_songs():
    spotify_ids = []
    groups = client.groups.list(omit="memberships")
    for i in groups:
        if i.name == "Sigma Flips and Flops, Drips and Drops":
            group = i

    for message in group.messages.list_all():
        i = str(message.text)                   # i is a single messages
        whole_link = message.text                                
        if i.startswith('https://open.spotify.com/track/') :
            spotify_ids.append(whole_link[31:53])

    return spotify_ids

# Takes in a list of Spotify ID's
# adds them to a specified playlist
def add_to_playlist(track_ids):
    scope = 'playlist-modify-public'
    username = 'Cobbles333'
    token = util.prompt_for_user_token(username,
                            scope,
                            client_id='ad0d6c5d68e4464fb777cbf0e85c4c03',
                            client_secret='f456c5b87cc74e8db505e69fbd58e77d',
                            redirect_uri='http://127.0.0.1:8878')
    
    playlist_id = "1QsFdKLlXNHfA8msOwPWLw"

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print(results)
    else:
        print("Can't get token for", username)

#### RUN:####
spotify_ids = get_songs()
print(spotify_ids)
top_50 = spotify_ids[0:50]
add_to_playlist(top_50)





