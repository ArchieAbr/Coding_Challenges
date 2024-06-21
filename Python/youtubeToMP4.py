import ssl
import sys
import socket
from pytube import YouTube

# Set up
ssl._create_default_https_context = ssl._create_unverified_context
SAVE_PATH = "/Users/archie/Desktop/Youtube_Videos"


def test_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


# Function to handle downloading
def download(link):
    youtube_object = YouTube(link)
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
        sys.exit(1)



def main():
    if not test_connection():
        print("No internet connection.")
        return
    print("Checking connection...")
    print("Connection established.\n")
    link = input("Please copy the Youtube Video URL into the terminal\n")
    download(link)


if __name__ == "__main__":
    main()
