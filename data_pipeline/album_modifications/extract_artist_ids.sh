#!/bin/bash

# this script extracts all unique artist names present in scraped albums
json_file="data/albums/complete_data.json"

# Use jq to extract album_id from the "items" array
artist_ids=$(jq -r '.items[].artist_spotify_id' "$json_file")
id="data/artist_ids.txt"
unique_id="data/unique_artist_ids.txt"

# Iterate over the extracted album_ids 
# Add album ids to a file
for artist_id in $artist_ids; do
    echo "$artist_id" >> $id
done

# reduce album_ids to unique values
sort $id | uniq > $unique_id

rm $id