from pytube import YouTube, Playlist
import csv


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


def download_single_or_playlist(url):
    if "/watch?v=" in url:
        # Single YouTube video URL
        print("Downloading single video:", url)
        Download(url)
    elif "/playlist?list=" in url:
        # YouTube playlist URL
        print("Downloading playlist:", url)
        download_playlist(url)
    else:
        print("Invalid URL:", url)


def download_playlist(playlist_link):
    playlist = Playlist(playlist_link)
    for video_url in playlist.video_urls:
        print("Downloading:", video_url)
        Download(video_url)


# Read links from links.csv file
with open("links.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        url = row[0]
        download_single_or_playlist(url)
