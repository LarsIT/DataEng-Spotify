import re

with open("data/transferable_data/artists.txt", "r") as infile:
    dataset1 = infile.read()

with open("data/transferable_data/albums_artists.txt") as infile:
    dataset2 = infile.read()


ds1matches = []
ds2matches = []

pattern = r"'([^']+)'|\d+|(\w+)"

for row in dataset1.splitlines():

    matches = re.findall(pattern, row)

    ds1matches.append(matches[0])

for row in dataset2.splitlines():
    matches = re.findall(pattern, row)

    ds2matches.append(matches[1])

ds1matches = list(set(ds1matches))
ds2matches = list(set(ds2matches))

# print(ds2matches)

# print(ds1matches)

res = ds1matches - ds2matches


print(res)





# # Find orphaned artist_ids
# orphaned_artist_ids = artist_ids_dataset1 - artist_ids_dataset2

# # Print orphaned artist_ids
# print("Orphaned artist_ids:")
# for artist_id in orphaned_artist_ids:
#     print(artist_id)