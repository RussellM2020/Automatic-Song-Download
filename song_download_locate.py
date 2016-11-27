#song download file
from song_copy import copy

def download_locate(song_url_list, song_list,album):
    import time
    import string
    import os
    from shutil import copyfile
    import selenium
    from selenium import webdriver

    loc_dic={}
    dow="C:\\Users\\Russell\\Downloads\\New Downloaded Music"
    index=0
    
    for song_url in song_url_list:
        
        profile = webdriver.FirefoxProfile('C:\Users\Russell\AppData\Roaming\Mozilla\Firefox\Profiles\qc8tc55i.default')
        browser = webdriver.Firefox(profile)
        browser.get('http://www.youtube-mp3.org/')
        element=browser.find_element_by_id('youtube-url')
        element.clear()
        element.send_keys(song_url)
        browser.find_element_by_id('submit').click()
        browser.implicitly_wait(15)
        browser.find_element_by_link_text('Download').click()

        #waiting one minute for download
        time.sleep(30)
        print "entered"

        #checking if download is complete, and then transfering file, closing browser
        song=song_list[index]
        
        i=0
        L= os.listdir(dow)
        while (i<len(L)):
            L= os.listdir(dow)
            #print L[i] _ _ _ for debugging
            splist=L[i].split(".")
            if splist[-1].lower()!="part":
                
                i=i+1
            else:
                #print "part file detected-waiting"_ _ _ for debugging
                time.sleep(15)
                i=0

        M=os.listdir(dow)
        for i in M:
            if song.title() in i.title():
                
                #copy(album, dow, dist, i, song)                   
                loc_dic[song]=i
           
        index=index+1
        browser.close()
    
    print loc_dic
    return loc_dic

