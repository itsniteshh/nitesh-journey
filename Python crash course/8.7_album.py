def make_album(artist_name, album_title, no_of_songs = None):
    #function which returns album details in a list
    if no_of_songs:
        album_details = {"Artist": artist_name,
                     "Album": album_title,
                     "Songs": no_of_songs}
    else:
        album_details = {"Artist": artist_name,
                     "Album": album_title}
    
    return album_details

about_album = make_album("Nitesh Jha", "This is my story", 1)
about_album = make_album("Nitesh ", "This is my goal", 2)
print(about_album)
    

    