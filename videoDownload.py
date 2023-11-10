# download_video.py
from pytube import YouTube
import sys

def download_video(video_url, output_directory):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()

        # Download the video
        video.download(output_directory)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = sys.argv[1]
    output_directory = sys.argv[2]
    download_video(video_url, output_directory)
