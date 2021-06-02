#from pytube import YouTube

#url = input("enter here the url of the video: ")
#ytd = YouTube(url).stream.filter(only_audio=True).download()

from __future__ import unicode_literals
import youtube_dl

url = input()

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
