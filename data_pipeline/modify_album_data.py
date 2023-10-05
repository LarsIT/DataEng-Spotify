import json
import pandas as pd
import os

def remove_items(data:dict, *args:str):
    ''' deletes keys specified in args from dictionary '''
    for keyword in args:
        data.pop(keyword)


# adjust file path for a loop when logic complete

# columns:
# album_group, album_type, artist, spotify_id, name, release_date, number_of_tracks

# file handling
filepath = 'data_pipeline/0DjR09NBgtZbkOnBZays9o_albums.json'
with open(filepath, 'r') as jsonfile:
    data = json.load(jsonfile)
    data = data['items']

# modifiy data

unwound_albums = []
# Iterate through albums

for album in data:

    # variables for ease of use
    artists = album['artists']
    artist_count = len(artists)

    # remove unnecessary data points
    remove_items(album, 'available_markets', 'external_urls', 'release_date_precision', 'uri', 'images', 'href')

    # duplicate entries for albums with multiple artists
    for i in range(0, artist_count):
        current_artist = album['artists'][i] # convenience variable
        
        new_album = album.copy() # create copy
        new_album.pop('artists') # remove artists list

        # set artist related values on higher level in hierarchy
        new_album['artist_name'] = current_artist['name']
        new_album['artist_spotify_id'] = current_artist['id']
        new_album['artist_type'] = current_artist['type']
        
        # rename attribute
        new_album['album_id'] = new_album['id']
        unwound_albums.append(new_album)
    


print(unwound_albums)
