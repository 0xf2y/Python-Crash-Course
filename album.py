def make_album(artist_name,album_title,num_of_songs=None):
    album={"name":artist_name,"title":album_title}
    if num_of_songs:
        album["num_of_songs"]=num_of_songs
    return album
album1=print(make_album("rihana","s&m",num_of_songs="1"))
album1=print(make_album("the weekend","after hours",num_of_songs="13"))
album1=print(make_album("shakira","shakira",num_of_songs="12"))

