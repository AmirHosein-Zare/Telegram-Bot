# requests library
import requests

#import packge for download image from url
from PIL import Image
import requests
import urllib.request
from io import BytesIO

def getpic(url):
    response = requests.get(url)
    img = Image.open(response.content,'rb')
    return img
    
def getPicture(url):
    urllib.request.urlretrieve(url,"new.jpg")
    img = Image.open("new.jpg")



# get movie from TMDB Api website
def getMovie(name):
    api_key = '2daf17455648c676bffaf192d612608c'
    
    try:
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={name}&language=en-US&page=1&include_adult=false')
    except:
        return ["Sorry, There is some problem to get request", "-1"]

    if response.status_code == 200:
        response_json = response.json()
        title = response_json['results'][0]['title']
        overview = response_json['results'][0]['overview']
        release_date = response_json['results'][0]['release_date']
        original_language = response_json['results'][0]['original_language']
        vote_average = response_json['results'][0]['vote_average']
        image = response_json['results'][0]['poster_path']
        text = f'''
Title:   {title}

Overview:   {overview}

Release Date:   {release_date}

Original Language:   {original_language}

Vote Average:   {vote_average}
        '''
        result = [text, image]
        return result
    else:
        return ["I can't Find This Film :(", "-1"]

def getStatus(name):
    api_key = '2daf17455648c676bffaf192d612608c'
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={name}&language=en-US&page=1&include_adult=false')
    return response.status_code