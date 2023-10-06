#!/bin/bash

# filepath from view of working directory of python interpreter
albums_folder="data/albums"
songs_folder="data/songs"
artists_folder="data/artists"

# remove folder contents
rm -rf "$albums_folder"/*
rm -rf "$artists_folder"/*
rm -rf "$songs_folder"/*
