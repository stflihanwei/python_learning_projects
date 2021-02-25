# Album make_album() take in artist name and an album title, and it should return a dictionary containing
# these information. Use the function to make three dictionaries representing different albums.
# print each return value to show that the dictionaries are storing the album information correctly
# add an optional parameter, allow you to store the number of tracks on an album.

def make_album(artist_firstname, artist_lastname, album_title, track_number=''):  # track_number is a optional variable
    album = {'Artist Firstname': artist_firstname, 'Artist Lastname': artist_lastname,
             'Album Title': album_title, 'Track Number': track_number}
    if track_number:
        album['track number'] = track_number
    return album

# use a while loop to make user enter album details
while True:
    print("\nPlease enter an album's information ")
    print("Enter 'q' to exit")

    a_fname = input("Artist firstname:")
    if a_fname == 'q':
        break
    a_lname = input("Artist lastname:")
    if a_lname == 'q':
        break
    a_title = input("Album title:")
    if a_title == 'q':
        break
    a_tracknmbr = input("Album tracknumber (optional):")
    if a_tracknmbr == 'q':
        break
    album_info = make_album(a_fname, a_lname,a_title, a_tracknmbr)
    print(album_info)


album1 = make_album('Jimi', 'Ray','The tale of 1900', track_number=27)
print(album1)
print('Artist name:' + album1['artist firstname'] +' ' + album1['artist lastname'])

album2 = make_album('Chen', 'Lu', 'Circus')
print(album2)
