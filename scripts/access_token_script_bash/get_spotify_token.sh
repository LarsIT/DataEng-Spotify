#!/bin/bash

# Clear response file
> "scripts/access_token_script_bash/access_response.json"

credentials="scripts/access_token_script_bash/credentials.json"

# Setting variables
client_id=$(jq -r '.client_id' $credentials)
client_secret=$(jq -r '.client_secret' $credentials)

# Send request for access token and save it to file
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=$client_id&client_secret=$client_secret" \
     >> "scripts/access_token_script_bash/access_response.json"
