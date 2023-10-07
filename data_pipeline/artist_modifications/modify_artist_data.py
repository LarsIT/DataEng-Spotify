import os
import json
import subprocess

def remove_items(data:dict, *args:str):
    ''' deletes keys specified in args from dictionary '''
    for keyword in args:
        data.pop(keyword)

# each artist file is for one artist

# data points of interest:
# name, popularity, type, id, follower, genres
unwound_data = []

# TODO add iteration through artist directory 
artist_files = os.listdir("data/artists")

for artist in artist_files:
        
    with open(f"data/artists/{artist}", 'r') as jsonfile:
        data = json.load(jsonfile)
    
    genre_count = len(data["genres"])


    remove_items(data, "external_urls", "href", "images", "uri")

    
    # duplicate entries for albums with multiple artists
    for i in range(0, genre_count):
        current_genre = data['genres'][i] # convenience variable
        
        new_artist = data.copy() # create copy
        new_artist.pop('genres') # remove data structure "genres"

        new_artist['genre'] = current_genre
        new_artist['followers'] = new_artist['followers']['total']

        unwound_data.append(new_artist)


# remove old data (artist)
bash_script_path = 'data_pipeline/artist_modifications/remove_old_artist_data.sh'

# Use subprocess to execute the Bash script
try:
    subprocess.run(['bash', bash_script_path], check=True)
    print('Old Artist Data Removal Successful .')
except subprocess.CalledProcessError as e:
    print(f'Error: Bash script execution failed with return code {e.returncode}.')
except FileNotFoundError:
    print('Error: Bash script not found.')
# save cleaned data

clean_data = {'items' : unwound_data} 
with open('data/artists/complete_data.json', 'w') as jsonfile:
    json.dump(clean_data, jsonfile, indent=6)








