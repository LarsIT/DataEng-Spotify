import json

# transform album data into 3rd norm

with open("data/albums/complete_data.json", "r") as readfile:
    data = json.load(readfile)

albums = []
albums_artists_relation = []

for item in data["items"]:

    # album values
    album_id = str(item["album_id"])
    album_type = str(item["album_type"])
    name = str(item["name"])
    total_tracks = int(item["total_tracks"])
    release_date = str(item["release_date"])

    albums.append(
        (album_id, album_type, name, total_tracks, release_date)
    )

    # album_artist values
    artist_id = str(item["artist_spotify_id"])

    albums_artists_relation.append(
        (album_id, artist_id)
    )

albums = list(set(albums))

# write values for albums insertion
with open("data/transferable_data/albums.txt", "w") as outfile:
    for album in albums:
        outfile.write(f"{album}, \n")

with open("data/transferable_data/albums_artists.txt", "w") as outfile:
    for relation in albums_artists_relation:
        outfile.write(f"{relation}, \n")
