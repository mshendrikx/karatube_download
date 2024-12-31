from flask import Flask, jsonify
from pytubefix import YouTube

YT_BASE_URL = "https://www.youtube.com/watch?v="

app = Flask(__name__)

@app.route('/<youtubeid>')
def youtube_download(youtubeid):

    video_file = str(youtubeid) + ".mp4"
    file_path = '/app/download'
    download_url = YT_BASE_URL + str(youtubeid)
    try:
        YouTube(download_url).streams.first().download(output_path=file_path, filename=video_file)
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7006)
        