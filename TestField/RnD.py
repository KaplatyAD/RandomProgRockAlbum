import requests
import random

from Config import Config
config = Config()
random_page = random.randint(1, 200)
random_item = random.randint(1, 50)
def get_album():
    test = requests.get(f'https://api.discogs.com/database/search?style=prog+rock&page{random_page}&token={config._DISCOGS_TOKEN}')

    album_cover = test.json()['results'][random_item]['cover_image']
    artist = test.json()['results'][random_item]['title'].split('-')[0]

    return artist, album_cover

