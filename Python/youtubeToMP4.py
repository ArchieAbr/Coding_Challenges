import ssl
from sys import exit
import socket
from pytube import YouTube
from tqdm import tqdm

# Set up
ssl._create_default_https_context = ssl._create_unverified_context
SAVE_PATH = "/Users/archie/Desktop/Youtube_Videos"


def check_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def progress_function(stream, chunk, bytes_remaining):
    current = stream.filsize - bytes_remaining
    percent = (current / stream.filesize) * 100
    print(f"Progress {percent}%", end='\r')


# Function to handle downloading
def download(link):
    youtube_object = YouTube(link,on_complete_callback=progress_function)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        title = youtube_object.title
        file_size = youtube_object.filesize_mb
        print("Found video:", title)
        print("Approx. file size:", file_size, "MB")
        print("Downloading Video...\n")
        youtube_object.download(output_path=SAVE_PATH)
        print("Download completed successfully, video is can be found here:", SAVE_PATH, "\n")
    except:
        print("An error has occurred while trying to download your video, please check your network connection\n")
        exit(1)


def main():
    if not check_connection():
        print("No internet connection. Please try again")
        exit(1)
    print("Checking connection...")
    print("Connection established.\n")
    link = input("Please copy the Youtube Video URL into the terminal\n")
    download(link)


if __name__ == "__main__":
    main()
