import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox

# Folder to save videos
SAVE_FOLDER = r"E:\youtube"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def download_video():
    link = entry.get().strip()
    if not link:
        messagebox.showwarning("Input Error", "Please paste a video link!")
        return

    try:
        ydl_opts = {
            'outtmpl': os.path.join(SAVE_FOLDER, '%(title)s.%(ext)s'),
            'format': 'best[ext=mp4]'  # single stream, avoids ffmpeg merge
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def exit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Video Downloader")
root.geometry("500x200")

label = tk.Label(root, text="Paste video link (YouTube or other supported sites):")
label.pack(pady=10)

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

root.mainloop()