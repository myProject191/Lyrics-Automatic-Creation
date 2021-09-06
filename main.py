import os
from flask import Flask
from flask import request, render_template, send_from_directory
import markov_short as markov

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/", methods=["POST"])
def post():
    number = request.form['select_artist']
    lyrics = markov.sentence(number)
    artist_name = markov.artist_name(number)
    return render_template('index.html', lyrics = lyrics, artist_name = artist_name)



app.run(port=8000, debug=True)