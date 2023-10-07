#!/bin/bash

# filepath from view of working directory of python interpreter
folder="data/songs"

# remove folder contents
rm -rf "${folder:?}"/*

