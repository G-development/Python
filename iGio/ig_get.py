import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

def getUserLink(user):
    URL = f"http://instagram.com/{user}/"
    return URL

def getStories(user):
    userStoriesLink = f"http://instagram.com/stories/{user}/"
    return userStoriesLink





#getUserLink("ciao")
#getStories("anabnormalguy")