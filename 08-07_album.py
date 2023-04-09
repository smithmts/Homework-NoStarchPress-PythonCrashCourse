# Write a function called make_album() that builds a dictionary
# describing a music album.
# Should take an artist name and album title, and return a dictionary
# With those two pieces of information.
# Use optional parameter for number of songs on the album.
# Call at least three three times, one with number of songs.

def make_album(album_name, artist, num_of_songs=None):
    """Build a dictionary with album information"""
    album = {
            'album_name': album_name,
            'artist': artist,
            }
    if num_of_songs:
        album['num_of_songs'] = num_of_songs
    return album


album = make_album('stone cold rhymin', 'young MC')
print(album)

album = make_album('living things', 'linkin park')
print(album)

album = make_album('typhoons', 'royal blood', 11)
print(album)
