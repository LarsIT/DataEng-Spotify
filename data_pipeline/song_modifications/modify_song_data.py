import os
import json
import subprocess

# each file is an album worht of songs
# each item in items is a song
# reduce songs to interesting data points:
#   album_id, artist_name, artist_id, song_duration, explicit_flag, song_id, song_name, song_number_on_album 
# get all songs into one document 

with open("data/songs/5095tKCLWklnaq2NNdID2h_songs.json") as jsonfile:
    data = json.load(jsonfile)

album_id = data["href"].split("/")[-2]

album = data["items"]

for song in album:
    print(song)
    break