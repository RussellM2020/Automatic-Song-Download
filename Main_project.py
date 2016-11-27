#main file of project
import os
from song_url import get_songs
from song_download_locate import download_locate
from song_tags import tags


print "Welcome to the album mp3 generator"
print
while True:
    album=raw_input("Enter name of the Album")
    artist=raw_input("Enter name of the artist")
    year=int(raw_input("Enter year"))
    song_list=[]
    
    num=int(raw_input("How many songs in this album?"))
    for i in range(num):
        a=raw_input("Enter the songs for this album, in order")
        song_list.append(a)

    song_url_list=get_songs(artist, song_list)        
    loc_dic=download_locate(song_url_list, song_list, album)
    tags(album, artist, year, loc_dic, song_list)
    
    
    flag=raw_input("Please type Quit if you want to leave the application")
    if flag.title()=="Quit":
        print "Thank You"
        break
    
    
#TO DO make a folder only if it isn't there
#Learn how to deal with pop up , alert
#set tags appropriately
    
