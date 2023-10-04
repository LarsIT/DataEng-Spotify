@echo off

REM clear response file
type NUL > access_response.json

REM setting variables
set client_id=9b56e17041b04d64acc80768210ba27d
set client_secret=bbd0a6c21c1a4a0096b562b9481ac07a

REM send request for access token and save it to file
curl -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=%client_id%&client_secret=%client_secret%" >> access_response.json
