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


# Progress bar
def progress_function(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    progress_bar.update(current - progress_function.prev)
    progress_function.prev = current


# Function to handle downloading
def download(link):
    youtube_object = YouTube(link, on_progress_callback=progress_function)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        title = youtube_object.title
        file_size = youtube_object.filesize_mb
        print("Found video:", title)
        print("Approx. file size:", file_size, "MB")
        print("Downloading Video...")
        global progress_bar
        progress_bar = tqdm(total=youtube_object.filesize, unit='B', unit_scale=True)
        progress_function.prev = 0
        youtube_object.download(output_path=SAVE_PATH)
        progress_bar.close()
        print("Download completed successfully, video is can be found here:", SAVE_PATH, "\n")
        exit(0)
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
