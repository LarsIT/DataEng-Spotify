#!/bin/bash

json_file="../../data/albums/complete_data.json"

# Use jq to extract album_id from the "items" array
artist_ids=$(jq -r '.items[].artist_spotify_id' "$json_file")

# Iterate over the extracted album_ids 
# Add album ids to a file
for artist_id in $artist_ids; do
    echo "$artist_id" >> artist_ids.txt
done

# reduce album_ids to unique values
sort artist_ids.txt | uniq > unique_artist_ids.txt

rm artist_ids.txt