from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            download_video(url)
        return render_template('index.html', success=True)
    return render_template('index.html', success=False)

def download_video(url):
    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        download_folder = 'YTdownloads'
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        yd = yt.streams.get_highest_resolution()
        yd.download(download_folder)
        print("Download complete.")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
