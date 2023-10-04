#!/bin/bash

# Clear response file
> access_response.json

# Setting variables
client_id=$(jq -r '.client_id' credentials.json)
client_secret=$(jq -r '.client_secret' credentials.json)

# Send request for access token and save it to file
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=$client_id&client_secret=$client_secret" \
     >> access_response.json
