import pytube
import os

class Download:

    def __init__(self):
        self.total_videos = 0
        self.current_video = 0
        self.progress_var = None

    def set_progress_var(self, progress_var):
        self.progress_var = progress_var

    def downloadVideo(self, url, download_type="mp4"):
        try:
            video = pytube.YouTube(url)
            stream = video.streams.get_lowest_resolution()

            file_extension = ".mp4" if download_type == "mp4" else ".mp3"

            download_directory = "Downloads"
            os.makedirs(download_directory, exist_ok=True)

            self.total_videos = 1
            self.current_video = 0
            self.show_progress()
            filename = f"{video.title}{file_extension}"
            filepath = os.path.join(download_directory, filename)
            stream.download(filename=filename)
            self.progress_var.set(f"Download Complete: {filename}")

        except pytube.exceptions.VideoUnavailable:
            self.progress_var.set("Error: Video is unavailable for download.")
        except Exception as e:
            self.progress_var.set(f"An error occurred during the download: {str(e)}")

    def downloadPlaylist(self, playlist_url, download_type="mp4"):
        try:
            playlist = pytube.Playlist(playlist_url)
            
            download_directory = "Downloads"
            os.makedirs(download_directory, exist_ok=True)

            playlist_name = "Playlist"
            if playlist.title:
                playlist_name = playlist.title
            playlist_directory = os.path.join(download_directory, playlist_name)
            os.makedirs(playlist_directory, exist_ok=True)

            self.total_videos = len(playlist.video_urls)
            self.current_video = 0
            self.show_progress()

            for video_url in playlist.video_urls:
                video = pytube.YouTube(video_url)
                stream = video.streams.get_lowest_resolution()

                file_extension = ".mp4" if download_type == "mp4" else ".mp3"

                self.current_video += 1
                self.show_progress()
                filename = f"{video.title}{file_extension}"
                filepath = os.path.join(playlist_directory, filename)
                stream.download(filename=filename)
                self.progress_var.set(f"Download Complete: {filename}")

            self.progress_var.set(f"Playlist Download Complete: {playlist_name}")

        except Exception as e:
            self.progress_var.set(f"An error occurred during playlist download: {str(e)}")

    def show_progress(self):
        if self.total_videos > 1:
            progress_text = f"Video {self.current_video} of {self.total_videos} completed"
        elif self.total_videos == 1:
            progress_text = "Download completed"
        else:
            progress_text = ""

        if self.progress_var:
            self.progress_var.set(progress_text)
