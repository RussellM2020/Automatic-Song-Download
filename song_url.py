#get_songs() function

def get_songs(artist, song_list):
    import urllib
    import urllib2
    from bs4 import BeautifulSoup
    song_list_urls=[]
    for song in song_list:
        textToSearch = song+artist
        url = "https://www.youtube.com/results?search_query=" + urllib.quote(textToSearch)
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        vid=soup.findAll(attrs={'class':'yt-uix-tile-link'})[0] #index 0 implies only first result taken
        song_list_urls.append('https://www.youtube.com' + vid['href'])
    return song_list_urls


