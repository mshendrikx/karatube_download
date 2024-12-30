from pytubefix import YouTube

YT_BASE_URL = "https://www.youtube.com/watch?v="

youtubeid = 'oEuBzpKF3X8'
video_file = str(youtubeid) + ".mp4"
filename = "/home/mauricio/temp/" + video_file
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

breakpoint