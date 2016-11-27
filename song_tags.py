#setting tags of songs

def tags(album, artist, year, loc_dic, song_list):
    import sys
    sys.path.append('C:\\Users\\Russell\\Desktop\\Python Programs\\dist\\mutagen-1.33.2')
    

    from mutagen.mp3 import MP3
    from mutagen.id3 import ID3NoHeaderError
    from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC
    index=1
    for song in song_list:
        print loc_dic
        location="C:\\Users\\Russell\\Downloads\\New Downloaded Music\\"+loc_dic[song]
        tags = ID3(location)
        tags["TIT2"] = TIT2(encoding=3, text=song)
        tags["TALB"] = TALB(encoding=3, text=album)
        tags["TPE2"] = TPE2(encoding=3, text=artist)
        tags["TPE1"] = TPE1(encoding=3, text=artist)
        tags["TDRC"] = TDRC(encoding=3, text=str(year))
        tags["TRCK"] = COMM(encoding=3, text=str(index))
        tags.save(location)
        index=index+1

     
