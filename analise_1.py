import pandas as pd 
import matplotlib as plt 
from main import get_audio_features,get_auth_header,get_token,get_songs_by_artist,search_for_track,search_for_artist
import json 

token = get_token()

artist_name = "Coldplay"

artist_id = search_for_artist(token,"Coldplay")["id"]

print(artist_id)
#get_songs_by_artist(token,artist_id)

