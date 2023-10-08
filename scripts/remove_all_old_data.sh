#!/bin/bash

# filepath from view of working directory of python interpreter
albums_folder="data/albums"
songs_folder="data/songs"
artists_folder="data/artists"
transfer_data_folder="data/transferable_data"
unique_artist_ids="data/unique_artist_ids.txt"
unique_album_ids="data/unique_album_ids.txt"

# remove folder contents
rm -rf "${albums_folder:?}"/*
rm -rf "${artists_folder:?}"/*
rm -rf "${songs_folder:?}"/*
rm -rf "${transfer_data_folder:?}"/*
rm -rf "${unique_artist_ids:?}"
rm -rf "${unique_album_ids:?}"
