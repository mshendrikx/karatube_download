from flask import Flask, jsonify
from pytubefix import YouTube

YT_BASE_URL = "https://www.youtube.com/watch?v="

app = Flask(__name__)

@app.route('/<youtubeid>')
def youtube_download(youtubeid):

    video_file = str(youtubeid) + ".mp4"
    filename = "/app/download/" + video_file
    download_url = YT_BASE_URL + str(youtubeid)
    try:
        YouTube(download_url).streams.first().download(filename=filename)
        downloaded = 1
        error_string = ''
    except Exception as e:
        downloaded = 0
        error_string = e.error_string
    dados = { 
            'downloaded': downloaded,
            'error_string': error_string
    }
    
    return jsonify(dados)
        