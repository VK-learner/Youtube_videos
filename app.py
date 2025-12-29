import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox
import threading

SAVE_FOLDER = r"E:\youtube"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            percent = downloaded / total * 100
            status_label.config(text=f"Downloading... {percent:.2f}%")
            root.update_idletasks()  # force GUI refresh
        else:
            status_label.config(text="Downloading... size unknown")
    elif d['status'] == 'finished':
        status_label.config(text="Download completed!")
    elif d['status'] == 'error':
        status_label.config(text="Download failed!")

def start_download():
    link = entry.get().strip()
    if not link:
        messagebox.showwarning("Input Error", "Please paste a video link!")
        return

    def run_download():
        try:
            ydl_opts = {
                'outtmpl': os.path.join(SAVE_FOLDER, '%(title)s.%(ext)s'),
                'format': 'best[ext=mp4]',
                'progress_hooks': [progress_hook]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except Exception as e:
            status_label.config(text="Download failed!")
            messagebox.showerror("Error", str(e))

    threading.Thread(target=run_download, daemon=True).start()

def exit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Video Downloader")
root.geometry("500x220")

label = tk.Label(root, text="Paste video link:")
label.pack(pady=10)

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

download_button = tk.Button(root, text="Download", command=start_download)
download_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=10)

root.mainloop()