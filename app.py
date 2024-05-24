from flask import Flask, request, render_template, jsonify
from TestField import RnD
import requests
from random import randrange
from Config import Config
app = Flask(__name__)
config = Config()



@app.route('/')
def random_album():  # put application's code here
    random_page = randrange(1, 199)
    random_item = randrange(1, 49)
    test = requests.get(
        f'https://api.discogs.com/database/search?style=prog+rock&page{random_page}&token={config._DISCOGS_TOKEN}')
    if test.status_code == 200:
        response = test.json()
        album_cover = response['results'][random_item]['cover_image']
        artist = response['results'][random_item]['title'].split('-')[0]
        album_name = response['results'][random_item]['title'].split('-')[-1]
        year = response['results'][random_item]['year']
        country = response['results'][random_item]['country']
        get_tracks = requests.get(response['results'][random_item]['resource_url'])
        tracks = get_tracks.json()
        list_of_tracks = [(track['title'], track['duration']) if track['duration'] else (track['title'], 'No data in DB') for
                          track in tracks['tracklist']
                          ]
        print(list_of_tracks)
        return render_template('album_page.html', artist=artist, album_image=album_cover,
                               album_title=album_name, year=year, country=country, list_of_tracks=list_of_tracks)
    return render_template('about.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
