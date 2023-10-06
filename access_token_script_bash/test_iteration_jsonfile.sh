#!/bin/bash

json_file="../data/albums/complete_data.json"

# Use jq to extract album_id from the "items" array
album_ids=$(jq -r '.items[].album_id' "$json_file")

# Iterate over the extracted album_ids 
# Add album ids to a file
for album_id in $album_ids; do
    echo "$album_id" >> album_ids.txt
done

# reduce album_ids to unique values
sort album_ids.txt | uniq > unique_album_ids.txt

rm album_ids.txt