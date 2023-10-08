import json

# prepare data for insertion into database

# genre entity type
genres = []
artists = []
artist_genre_relation = []

with open("data/artists/complete_data.json", "r") as artist_data:
    data = json.load(artist_data)

for item in data["items"]:
    # attributes for genres table
    genre = item["genre"]
    genres.append(genre)

    # attributes for artists table
    artist_id = str(item["id"])
    artist_name = str(item["name"])
    followers = item["followers"]
    popularity = item["popularity"]
    artist_type = str(item["type"])
    artists.append(
        (artist_id, artist_name, artist_type, followers, popularity)
    )

    # artists_genres relation values
    artist_genre_relation.append(
        (artist_id, genre)
    )

unique_genres = tuple(set(genres))
artists = list(set(artists))

# write values for genre insertion
with open("data/transferable_data/genres.txt", "w") as outfile:
    for genre in unique_genres:

        outfile.write(f"('{genre}'), \n")

# write values for artist insertion
with open("data/transferable_data/artists.txt", "w") as outfile:
    for artist in artists:

        outfile.write(f"{artist}, \n")

# write values for artist_genre relation insertion
with open("data/transferable_data/artists_genres.txt", "w") as outfile:
    for relation in artist_genre_relation:

        outfile.write(f"{relation}, \n")