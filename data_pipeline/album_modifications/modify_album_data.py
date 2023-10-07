import json
import os
import subprocess

def remove_items(data:dict, *args:str):
    ''' deletes keys specified in args from dictionary '''
    for keyword in args:
        data.pop(keyword)

unwound_albums = []
# adjust file path for a loop when logic complete
for artists_albums in os.listdir('data/albums'):

    # columns:
    # album_group, album_type, artist, spotify_id, name, release_date, number_of_tracks

    # file handling
    filepath = f'data/albums/{artists_albums}'
    with open(filepath, 'r') as jsonfile:
        data = json.load(jsonfile)
        data = data['items']

    # modifiy data


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
            new_album['album_id'] = new_album.pop('id')
            unwound_albums.append(new_album)
    



print(len(unwound_albums))

# remove old data (albums)
bash_script_path = 'data_pipeline/album_modifications/remove_old_data.sh'

# Use subprocess to execute the Bash script
try:
    subprocess.run(['bash', bash_script_path], check=True)
    print('Bash script executed successfully.')
except subprocess.CalledProcessError as e:
    print(f'Error: Bash script execution failed with return code {e.returncode}.')
except FileNotFoundError:
    print('Error: Bash script not found.')
# save cleaned data

clean_data = {'items' : unwound_albums} 
with open('data/albums/complete_data.json', 'w') as jsonfile:
    json.dump(clean_data, jsonfile, indent=6)
