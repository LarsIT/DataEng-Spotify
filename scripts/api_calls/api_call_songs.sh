#!/bin/bash

# path to access codes
access_file_path="scripts/access_token_script_bash/access_response.json"

# Extract access_token and token_type from access_response.json
access_token=$(jq -r '.access_token' $access_file_path)
token_type=$(jq -r '.token_type' $access_file_path)

# navigation variables
data_folder="data"
songs_folder="$data_folder/songs"

# Create the songs directory if it doesn't exist
if [ ! -d "$songs_folder" ]; then
    mkdir -p "$songs_folder"
fi

### API CALLS ###
# Get songs from scraped albums
unique_album_ids="data/unique_album_ids.txt"

while read -r line; do
# reading each line
    curl -X GET "https://api.spotify.com/v1/albums/$line/tracks?limit=50&offset=0" -H "Authorization: $token_type $access_token" -o "$songs_folder/${line}_songs.json"
done < $unique_album_ids

