import src.downloader as ytdl
import os

os.makedirs("output", exist_ok=True)
input_song = input("Enter youtube link or search: ")

ytdl.main(song=input_song, open_folder=True)