import yt_dlp
import os
import re
import subprocess

def clean_title(title):
    # Remove invalid Windows filename characters
    return re.sub(r'[\\/*?:"<>|]', "", title)


def download_mp3(url_or_search):
    print("Downloading audio...")

    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'output/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }


    # Allow search queries
    if not url_or_search.startswith("http"):
        url_or_search = f"ytsearch1:{url_or_search}"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url_or_search, download=True)

        # If it was a search, extract actual video info
        if 'entries' in info:
            info = info['entries'][0]

        #title = clean_title(info['title'])
        title = info['title']
        print(f"Downloaded: {title}.mp3")

    return title


def open_containing_folder(file_path):
    file_path = os.path.abspath(file_path)
    subprocess.run(['explorer', '/select,', file_path])


def main(song = None, output_folder=None, open_folder=False):    
    title = download_mp3(song)
    if not output_folder:
        os.makedirs("output", exist_ok=True)
        output_folder = "output"
    if open_folder: open_containing_folder(f"{output_folder}/{title}.mp3")