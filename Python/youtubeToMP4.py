from pytube import YouTube

# Set up
SAVE_PATH = "/Users/archie/Desktop/Youtube_Videos"
link = input("Please copy the Youtube Video URL into the terminal\n")


# Function to handle downloading
def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=SAVE_PATH)
    except:
        print("An error has occurred while trying to download your video, please check your network connection\n")
    print("Download completed successfully to:", SAVE_PATH, "\n")


download(link)
