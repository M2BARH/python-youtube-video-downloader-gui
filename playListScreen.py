import tkinter as tk
from downloaderScript import Download

class PlaylistScreen(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Download Playlist")

        self.var = tk.StringVar()
        self.var.set("mp4")  # Default to MP4

        self.download_frame = tk.Frame(self)
        self.download_frame.pack(padx=12, pady=12)

        self.label = tk.Label(self.download_frame, text="Youtube Playlist Downloader", font=('Sans-serif', 16))
        self.label.pack(padx=10, pady=10)

        self.link_frame = tk.Frame(self.download_frame)
        self.link_frame.pack(padx=10, pady=10)
        self.link_frame.columnconfigure(0, weight=1)
        self.link_frame.columnconfigure(1, weight=1)

        self.link_title = tk.Label(self.link_frame, text="Playlist Link:", font=('Arial', 12))
        self.link_title.grid(row=0, column=0)

        self.link_entry = tk.Entry(self.link_frame, font=('Arial', 12))
        self.link_entry.grid(row=0, column=1)

        self.mp4_btn = tk.Radiobutton(self.download_frame, text="MP4", variable=self.var, value="mp4", font=('Sans-serif', 12))
        self.mp4_btn.pack(pady=10)
        self.mp3_btn = tk.Radiobutton(self.download_frame, text="MP3", variable=self.var, value="mp3", font=('Sans-serif', 12))
        self.mp3_btn.pack(pady=10)

        self.progress_var = tk.StringVar()
        self.progress_label = tk.Label(self.download_frame, textvariable=self.progress_var, font=('Arial', 12))
        self.progress_label.pack(pady=10)

        self.download_btn = tk.Button(self.download_frame, text="Download Playlist", font=('Sans-serif', 16),
                                      command=self.download_playlist)
        self.download_btn.pack(padx=12, pady=12)

        self.download = Download()
        self.download.set_progress_var(self.progress_var)

    def download_playlist(self):
        playlist_url = self.link_entry.get()
        download_type = self.var.get()
        self.download.downloadPlaylist(playlist_url, download_type)


if __name__ == '__main__':
    app = tk.Tk()
    playlist_screen = PlaylistScreen(app)
    playlist_screen.pack(side="top", fill="both", expand=True)
    app.mainloop()
