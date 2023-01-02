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

while True:
    #loop to add info 
    print("\nPress 'q' anytime to quit")
    
    print("\nEnter artist name: ")
    a_name = input()
    if a_name == "q":
        break
    
    print("Enter album title: ")
    a_title = input()
    if a_title == "q":
        break
    
    

about_album = make_album(a_name, a_title)

print(about_album)
    

    