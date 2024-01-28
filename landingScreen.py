import tkinter as tk
from singleVideoScreen import SingleVideoScreen
from playListScreen import PlaylistScreen

class LandingScreen(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x550")
        self.master.title("Youtube Downloader")

        self.single_video_btn = tk.Button(self, text="Download Single Video", font=('Sans-serif', 16),
                                          command=self.show_single_video_screen)
        self.single_video_btn.pack(pady=20)

        self.playlist_btn = tk.Button(self, text="Download Playlist", font=('Sans-serif', 16),
                                      command=self.show_playlist_screen)
        self.playlist_btn.pack(pady=20)

        self.single_video_screen = SingleVideoScreen(self.master)
        self.playlist_screen = PlaylistScreen(self.master)

        self.single_video_screen.pack_forget()  # Hide initially
        self.playlist_screen.pack_forget()  # Hide initially

    def show_single_video_screen(self):
        self.playlist_screen.pack_forget()  # Hide playlist screen
        self.single_video_screen.pack()  # Show single video screen

    def show_playlist_screen(self):
        self.single_video_screen.pack_forget()  # Hide single video screen
        self.playlist_screen.pack()  # Show playlist screen


if __name__ == '__main__':
    app = tk.Tk()
    landing_screen = LandingScreen(app)
    landing_screen.pack(side="top", fill="both", expand=True)
    app.mainloop()
