import requests
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

def getUserLink(user):
    URL = f"http://instagram.com/{user}/"
    return URL

def getStoriesLink(user):
    userStoriesLink = f"http://instagram.com/stories/{user}/"
    return userStoriesLink

def get_stories():
    print(getUserLink("anabnormalguy"))
    page = requests.get(getStoriesLink("anabnormalguy"), headers=headers)
    print(page)
    soup = BeautifulSoup(page.content, 'html.parser')

    profilePic = soup.find_all('img')
    print(profilePic)


url = "https://www.instagram.com/anabnormalguy/"
print (url)
r = urlopen(url) 
print(r.read())


#getUserLink("ciao")
#getStories("anabnormalguy")
#get_stories()