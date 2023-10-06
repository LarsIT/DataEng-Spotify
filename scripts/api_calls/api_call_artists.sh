#!/bin/bash

# path to access codes
access_file_path="scripts/access_token_script_bash/access_response.json"

# Extract access_token and token_type from access_response.json
access_token=$(jq -r '.access_token' $access_file_path)
token_type=$(jq -r '.token_type' $access_file_path)


# navigation variables
data_folder="data"
artists_folder="$data_folder/artists"

# Create the artists directory if it doesn't exist
if [ ! -d "$artists_folder" ]; then
    mkdir -p "$artists_folder"
fi

### API CALLS ###

# Get artist data from scraped albums
unique_artist_ids="data/unique_artist_ids.txt"

while read -r line; do
# reading each line
    curl -X GET "https://api.spotify.com/v1/artists/$line" -H "Authorization: $token_type $access_token" -o "$artists_folder/${line}_artists.json"
done < $unique_artist_ids