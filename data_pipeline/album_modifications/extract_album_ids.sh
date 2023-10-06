#!/bin/bash

### this script extracts all unique album ids ###

json_file="data/albums/complete_data.json"
id="data/album_ids.txt"
unuique_id="data/unique_album_ids.txt"

# Use jq to extract album_id from the "items" array
album_ids=$(jq -r '.items[].album_id' "$json_file")

# Iterate over the extracted album_ids 
# Add album ids to a file
for album_id in $album_ids; do
    echo "$album_id" >> $id
done

# reduce album_ids to unique values
sort $id | uniq > $unuique_id

rm $id