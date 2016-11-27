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
        flag=0
        L= os.listdir(dow)
        i=0
        while (i<len(L)):            
            splist=L[i].split(".")
            if splist[-1].lower()!="part":
                i=i+1
            else:
                print "part file detected-waiting"
                time.sleep(15)
                i=0
        

                
                    
                             
                elif song.title() in i.title():
                    flag=1
                    #copy(album, dow, dist, i, song)
                    
                    loc_dic[song]=i
                                     
                    break
            if flag==0:
                print "waiting"
                time.sleep(15)
            elif flag==1:
                break
                
        index=index+1
        browser.close()
    
    print loc_dic
    return loc_dic

