#song download file

def download(song_url_list):
    import selenium
    from selenium import webdriver
    for song in song_url_list:
        profile = webdriver.FirefoxProfile('C:\Users\Russell\AppData\Roaming\Mozilla\Firefox\Profiles\qc8tc55i.default')
        browser = webdriver.Firefox(profile)
        browser.get('http://www.youtube-mp3.org/')
        element=browser.find_element_by_id('youtube-url')
        element.clear()
        element.send_keys(song)
        browser.find_element_by_id('submit').click()
        browser.implicitly_wait(15)
        browser.find_element_by_link_text('Download').click()
        #browser.close()
