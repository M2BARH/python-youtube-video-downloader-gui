
import pytube


class Download:

    def __init__(self):
        pass

    @staticmethod
    def downloadVideo( url):
        video = pytube.Youtube(url)
        print("Title: ", video.title)
        stream = video.streams.get_highest_resolution()
        stream.download()
        print("Download Complete!")
