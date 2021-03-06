from Groupy.groupy.client import Client #https://pypi.org/project/GroupyAPI/
import spotipy #https://github.com/plamere/spotipy
import spotipy.util as util

#Groupme Credentials
token = "" #FIXME get from groupme API
group_name = "" #FIXME str: groupchat that you want to target
#Spotify Credentials
username = '' #FIXME Spotify username
client_id = '' #FIXME Found on Spotify Developer dashboard
client_secret = '' #FIXME Found on Spotify Developer dashboard
playlist_id = '' #FIXME Spotify playlist URI, found on actual playlist

client = Client.from_token(token)

# Searches a groupme group for spotify links
# returns a list of track ID's
def get_songs():
    spotify_ids = []
    groups = client.groups.list(omit="memberships")
    for i in groups:                                # Locates and sets your targeted groupchat to "group"
        if i.name == group_name: 
            group = i
    for message in group.messages.list_all():      # Searches through all messages for spotify links   
        message_str = str(message.text)                        
        if message_str.startswith('https://open.spotify.com/track/'):
            spotify_ids.append(message_str[31:53])

    return spotify_ids

# Takes in a list of Spotify ID's
# adds them to a specified playlist
def add_to_playlist(track_ids):
    scope = 'playlist-modify-public'
    token = util.prompt_for_user_token(username,
                            scope,
                            client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri='http://127.0.0.1:8878')

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print(results)
    else:
        print("Can't get token for", username)

#### RUN:####
spotify_ids = get_songs()
top_50 = spotify_ids[0:50] #Gets 50 most recent songs
add_to_playlist(top_50)
