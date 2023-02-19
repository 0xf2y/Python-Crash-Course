def make_album(artist_name,album_title):
    album={"name":artist_name,"title":album_title}
    return album
while True:
    print("\ntell me your artist info:")
    print("enter 'q' at any time to quit")
    a_name=input("please enter your artist name: ")
    if a_name == 'q':
        break
    a_title=input("please enter your album title: ")
    if a_title == 'q':
        break
    album1=make_album(a_name,a_title)
    print(album1)