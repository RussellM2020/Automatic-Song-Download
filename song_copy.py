
def copy(album, dow, dist, i, song):
    from shutil import copyfile
   
    src=dow+"\\"+i
    d=dist+"\\"+song+".mp3"
    copyfile(src, d)

#copyfile("C:\\Users\\Russell\\Downloads\\New Downloaded Music\\OUR FATHER.mp3", "C:\\Users\\Russell\\Music\\New Christian Music\\jfk\\Our Father.mp3")
#copyfile("C:\\Users\\Russell\\Downloads\\New Downloaded Music\\OUR FATHER.mp3", dist+"\\"+song+".mp3")


