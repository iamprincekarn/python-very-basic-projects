from pytube import YouTube
link = "https://www.youtube.com/watch?v=4HRC6c5-2lQ&list=RD4HRC6c5-2lQ&start_radio=1"

yt = YouTube(link)
# print(yt.title)
# print(yt.thumbnail_url)

## for getting all type of streams (for downloading audio or video)
videos = yt.streams
for i in list(enumerate(videos)):
    print(i)
strm = int(input("enter: "))
videos[strm].download()
print("Video is downloaded successfully")

# # for downloading only audio (manually changing options of downloading )
audio = yt.streams.filter(only_audio=True)
aud = list(enumerate(audio))
for i in aud:
    print(i)
strmAudio = int(input("Enter the resolution you want: "))
audio[strmAudio].download()
print("Audio downloaded successfully")



## for downloading whole playslist
from pytube import Playlist
py = Playlist("https://youtube.com/playlist?list=PLu0W_9lII9ahPP_vKgaLzfdBV9RutrbWJ")
# print(py.title)
print(f'downlaoding : {py.title}')
for video in py.videos:
    video.streams.first().download()
print("playlist downlaoded")