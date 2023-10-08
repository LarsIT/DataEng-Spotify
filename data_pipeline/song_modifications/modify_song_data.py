import os
import json
import subprocess


def remove_items(data:dict, *args:str):
    ''' deletes keys specified in args from dictionary '''
    for keyword in args:
        data.pop(keyword)


# each file is an album worth of songs
# each item in items is a song
# reduce songs to interesting data points:
#   album_id, artist_name, artist_id, song_duration, explicit_flag, song_id, song_name, song_number_on_album 
# get all songs into one document 

song_data = os.listdir("data/songs")
for album in song_data:
        
    with open(f"data/songs/{album}") as jsonfile:
        data = json.load(jsonfile)

    unwound_songs = []
    album_id = data["href"].split("/")[-2]

    album = data["items"]


    # unwinding artists data structure
    for song in album:
        
        artist_count = len(song["artists"])

        remove_items(song, "available_markets", "disc_number", "external_urls", "href", "preview_url", "uri")

        for artist in range(0,artist_count):
            current_artist = song["artists"][artist]

            new_song = song.copy()
            new_song.pop("artists")

            new_song['album_id'] = album_id
            new_song["artist_name"] = current_artist["name"]
            new_song["artist_id"] = current_artist["id"]
            new_song["artist_type"] = current_artist["type"]
            new_song["song_id"] = new_song.pop("id")
            
            unwound_songs.append(new_song)
            




# remove old data (artist)
bash_script_path = 'data_pipeline/song_modifications/remove_old_song_data.sh'

# Use subprocess to execute the Bash script
try:
    subprocess.run(['bash', bash_script_path], check=True)
    print('Old Song Data Removal Successful .')
except subprocess.CalledProcessError as e:
    print(f'Error: Bash script execution failed with return code {e.returncode}.')
except FileNotFoundError:
    print('Error: Bash script not found.')
# save cleaned data

clean_data = {'items' : unwound_songs} 
with open('data/songs/complete_data.json', 'w') as jsonfile:
    json.dump(clean_data, jsonfile, indent=6)
