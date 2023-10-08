import json

songs = []

with open("data/songs/complete_data.json", "r") as artist_data:
    data = json.load(artist_data)

for item in data["items"]:
    song_id = str(item["song_id"])
    name = str(item["name"])
    duration_ms = int(item["duration_ms"])
    is_local = item["is_local"]
    track_number = int(item["track_number"])
    album_id = str(item["album_id"])

    songs.append(
        (song_id, name, duration_ms, is_local, track_number, album_id)
    )

songs = list(set(songs))

with open("data/transferable_data/songs.txt", "w") as outfile:
    for song in songs:
        outfile.write(f"{song}, \n")
