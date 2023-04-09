# Start with activity 8-8 capturing artist and title.
# Write a `while` loop that allows users to enter an album's artist
# and title.
# Call make_album() wiht user's input and print the dictionary that is
# Created.
# Don't forget quit value in the `while` loop.

def make_album(album_name, artist):
    """Build a dictionary with album information"""
    album = {
            'album_name': album_name,
            'artist': artist,
            }
    return album


while True:
    print("\nPlease provide information about an album")
    print("(enter 'q' at any time to quit)")

    album_name = input("Album name: ")
    if album_name == 'q':
        break

    artist = input("Artist: ")
    if artist == 'q':
        break

    album = make_album(album_name, artist)
    print(f"\nAlbum Name: {album_name.title()}")
    print(f"Artist: {artist.title()}")
