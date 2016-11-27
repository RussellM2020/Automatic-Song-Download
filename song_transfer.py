#transfering files from Download to Album Folder

def transfer(song_list, dist):
    import string
    import os
    from shutil import copyfile
    loc_dic={}
    dow="C:\\Users\\Russell\\Downloads\\New Downloaded Music"
    L= os.listdir(dow)
    for song in song_list:
        for i in L:
            if song.title() in i.title():
                copyfile(dow+"\\"+i, dist+"\\"+song+".mp3")
                loc_dic[song]=i
    return loc_dic
   
