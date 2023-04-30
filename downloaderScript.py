
import pytube


class Download:

    def __init__(self):
        pass

    def downloadVideo(self, url):
        try:
            video = pytube.YouTube(url)
            stream = video.streams.get_lowest_resolution()
            stream.download()
            print("Download Complete")
        except pytube.exceptions.VideoUnavailable:
            print("Error: Video is unavailable for download.")
        except Exception as e:
            print(f"An error occured during the download: {str(e)}")
