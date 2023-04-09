def make_album(album_name, artist, num_of_songs=None):
    """Build a dictionary with album information"""
    album = {
            'album_name': album_name,
            'artist': artist,
            }
    if num_of_songs:
        album['num_of_songs'] = num_of_songs
    return album
