
import tkinter as tk
from downloaderScript import Download


class MyGUI:

    def __init__(self, master):
        self.master = master
        master.geometry("350x300")
        master.title("Youtube Video Downloader")

        self.downloadFrame = tk.Frame(master)
        self.downloadFrame.pack(padx=12, pady=12)

        self.label = tk.Label(self.downloadFrame, text="Youtube Video downloader", font=('Sans-serif', 16))
        self.label.pack(padx=10, pady=10)

        self.linkFrame = tk.Frame(self.downloadFrame)
        self.linkFrame.pack(padx=10, pady=10)
        self.linkFrame.columnconfigure(0, weight=1)
        self.linkFrame.columnconfigure(1, weight=1)

        self.linkTitle = tk.Label(self.linkFrame, text="Link:", font=('Arial', 12))
        self.linkTitle.grid(row=0, column=0)

        self.linkEntry = tk.Entry(self.linkFrame, font=('Arial', 12))
        self.linkEntry.grid(row=0, column=1)

        self.downloadBtn = tk.Button(self.downloadFrame, text="Download", font=('Sans-serif', 16),
                                     command=self.downloadVideo)
        self.downloadBtn.pack(padx=12, pady=12)

        self.download = Download()

    def downloadVideo(self):
        url = self.linkEntry.get()
        self.download.downloadVideo(url)
        print("Download Complete!")


if __name__ == '__main__':
    app = tk.Tk()
    gui = MyGUI(app)
    app.mainloop()
