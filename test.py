# Sample data structure
albums = [
    {
        "album_name": "Album 1",
        "artists": [{"name": "Artist A", "id": "123"}, {"name": "Artist B", "id": "456"}]
    },
    {
        "album_name": "Album 2",
        "artists": [{"name": "Artist C", "id": "789"}]
    }
    # ... more album entries
]

unwound_albums = []
# Iterate through albums
# move the modified albums into unwound albums
# trash the old albums list

for album in albums:
    # variables for ease of use
    artists = album['artists']
    artist_count = len(artists)

    # duplicate entries for albums with multiple artists
    for i in range(0, artist_count):
        current_artist = album['artists'][i] # convenience variable
        
        new_album = album.copy() # create copy
        new_album.pop('artists') # remove artists list

        # set artist related values on higher level in hierarchy
        new_album['artist_name'] = current_artist['name']
        new_album['artist_spotify_id'] = current_artist['id']
        # new_album['artist_type'] = current_artist['type']
        
        unwound_albums.append(new_album)


print(unwound_albums)