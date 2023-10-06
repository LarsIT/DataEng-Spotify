#!/bin/bash

# path to access codes
access_file_path="../../access_token_script_bash/access_response.json"

# Extract access_token and token_type from access_response.json
access_token=$(jq -r '.access_token' $access_file_path)
token_type=$(jq -r '.token_type' $access_file_path)

# Spotify artist IDs
spotify_ids="0fN3Kd9aGNr9lTzRFqih4S 5TjlxSJvfrD5I2PWaEh4jZ 5fsDcuclIe8ZiBD5P787K1 0hEurMDQu99nJRq8pTxO14 0k17h0D3J5VfsdmQ1iZtE9 51Blml2LZPmy7TTiAg47vQ 3Nrfpe0tUJi4K4DXYWgMUX 6mGp1hXgz27GRQOkHD8d5m 41MozSoPIsD1dJM0CLPjZF 2kS9NyuATpYwjeB93h24H5 2KC9Qb60EaY0kW4eH68vr3 3WrFJ7ztbogyGnTHbHJFl2 711MCceyCBcFnzjGY4Q7Un 2ye2Wgw4gimLv2eAKyk1NB 2gCsNOpiBaMNh20jQ5prf0 1dfeR4HaWDbWqFHLkxsg1d 74oJ4qxwOZvX6oSsu1DGnw 0Y5tJX1MQlPlqiwlOH1tJY 6XyY86QOPPrYVGvF9ch6wz 6pAuTi6FXi6qFQJ1dzMXQs 7vk5e3vY1uw9plTHJAMwjN 3oDbviiivRWhXwIE8hxkVV 53XhwfbYqKCa1cC15pYq2q 7EQ0qTo7fWT7DPxmxtSYEc 3YQKmKGau1PzlVlkL1iodx 3UCbp6D1lvILlxRJT9LnFa 64N3o9z76C2APyfgQV2HMp 0lcOO2pXTNgXWPcOgFQnMf 2RJBv9wXbW6m539q9NOfW1 5j4HeCoUlzhfWtjAfM1acR 7n2Ycct7Beij7Dj7meI4X0 0FEJqmeLRzsXj8hgcZaAyB 0DjR09NBgtZbkOnBZays9o 4PfKPdq8QEgcerLwGApWIp 2FovgCfOwN9iqbkCBlKFdT 1nRbtbdYK51y71nVOxu332 7jVv8c5Fj3E9VhNjxT4snq 329e4yvIujISKGKz1BZZbO 3z97WMRi731dCvKklIf2X6 3L8FZaw2Rg1oUw3vB4gUME 6YVMFz59CuY7ngCxTxjpxE 2dIgFjalVxs4ThymZ67YCE 2q3GG88dVwuQPF4FmySr9I 3e7awlrlDSwF3iM0WBjGMp 4jCGRzuZkwo8CxboiANMEU 3UwlejyX2b458azZ7eCnHb 5RR0MLwcjc87wjSw2JYdwx 1IueXOQyABrMOprrzwQJWN 2AfmfGFbe0A0WsTYm0SDTx 13kJgvU22LHMsJtGWLmx7W 6mEQK9m2krja6X1cfsAjfl 5V1qsQHdXNm4ZEZHWvFnqQ 6MoXcK2GyGg7FIyxPU5yW6 7bmYpVgQub656uNTu6qGNQ 3nGqUwkJHiLPDECMVrX1Sq"

# navigation variables
data_folder="../../data"
albums_folder="$data_folder/albums"
songs_folder="$data_folder/songs"

# Create the albums directory if it doesn't exist
if [ ! -d "$albums_folder" ]; then
    mkdir -p "$albums_folder"
fi

# Create the albums directory if it doesn't exist
if [ ! -d "$songs_folder" ]; then
    mkdir -p "$songs_folder"
fi

### API CALLS ###

# # Get albums for each artist listed in spotify_ids
# for artist_id in $spotify_ids; do
#     curl -X GET "https://api.spotify.com/v1/artists/$artist_id/albums" -H "Authorization: $token_type $access_token" -o "$albums_folder/${artist_id}_albums.json"
# done

# Get songs from scraped albums

unique_album_ids="../album_modifications/unique_album_ids.txt"

while read line; do
# reading each line
    curl -X GET "https://api.spotify.com/v1/albums/$line/tracks?limit=50&offset=0" -H "Authorization: $token_type $access_token" -o "$songs_folder/${line}.json"
done < $unique_album_ids

# Get artist data from scraped albums
