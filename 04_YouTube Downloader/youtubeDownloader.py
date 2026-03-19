##TODO make a Youtube video downloader using pytube, tkinter

from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive = True, file_extension = "mp4")
        hiRes = streams.get_highest_resolution()
        hiRes.download(output_path = save_path)
        print(f'Downloading: {yt.title}')
    except Exception as e:
        print(e)

print("Welcome to the YouTube downloader!")
url = input("Enter URL: ")
save_path = "Save file goes here" #This is where the video will be downloaded, can be adjusted according to the user

download_video(url, save_path)
