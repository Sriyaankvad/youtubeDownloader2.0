from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import *
import os
from datetime import datetime

# Change the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

dest = './downloads/'


def download(link):
    try:
        # Download video as mp4
        # This is needed due to a bug on mac that leaves downloaded mp3 files corrupted
        # Will convert into mp3 later using moviepy
        yt = YouTube(link, on_progress_callback=on_progress)
        print(yt.title)
        input_vid = 'temp.mp4'

        ys = yt.streams.get_highest_resolution()
        ys.download(mp3=False, filename=input_vid)

        # Convert to mp3
        output_vid = dest + '' + yt.title + '.mp3'
        video = VideoFileClip(input_vid)
        video.audio.write_audiofile(output_vid)

        # Delete mp4 file
        os.remove(input_vid)
    except Exception as e:
        error_text(f'{type(e).__name__} Downloading: {link}. {e}\n')


def error_text(message):
    (open(f'{dest}error_log_{datetime.now()}.txt', 'a')).write(message)


def main():
    # Open file
    with open('links.txt', 'r') as file:
        links = file.readlines()

    # Get download location
    path = links[0].strip()

    # Check if download location exists. Download to default directory if doesn't
    if path == '' or not os.path.exists(path):
        print(f'Path {path} does not exist')
    else:
        if path[-1] != '/':
            path += '/'

        global dest
        dest = path

    # Download the links
    for link in links[1:]:
        link = link.strip()
        if link:
            download(link)


main()
