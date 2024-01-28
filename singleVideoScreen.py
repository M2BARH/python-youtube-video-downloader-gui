import tkinter as tk
from downloaderScript import Download

class SingleVideoScreen(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Download Single Video")  # Set the title directly on the master

        self.download_frame = tk.Frame(self)
        self.download_frame.pack(padx=12, pady=12)

        self.label = tk.Label(self.download_frame, text="Youtube Single Video Downloader", font=('Sans-serif', 16))
        self.label.pack(padx=10, pady=10)

        self.link_frame = tk.Frame(self.download_frame)
        self.link_frame.pack(padx=10, pady=10)
        self.link_frame.columnconfigure(0, weight=1)
        self.link_frame.columnconfigure(1, weight=1)

        self.link_title = tk.Label(self.link_frame, text="Video Link:", font=('Arial', 12))
        self.link_title.grid(row=0, column=0)

        self.link_entry = tk.Entry(self.link_frame, font=('Arial', 12))
        self.link_entry.grid(row=0, column=1)

        self.download_btn = tk.Button(self.download_frame, text="Download", font=('Sans-serif', 16),
                                      command=self.download_video)
        self.download_btn.pack(padx=12, pady=12)

        self.download = Download()

    def download_video(self):
        url = self.link_entry.get()
        self.download.downloadVideo(url)


if __name__ == '__main__':
    app = tk.Tk()
    single_video_screen = SingleVideoScreen(app)
    single_video_screen.pack(side="top", fill="both", expand=True)
    app.mainloop()
