import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import winsound

SAVE_FOLDER = r"E:\youtube"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# Keep track of download history
download_history = []

def play_bell():
    # Loud "ding-dong" bell effect
    winsound.Beep(2000, 400)   # sharp high pitch
    winsound.Beep(1000, 600)   # deeper tone

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            percent = downloaded / total * 100
            status_label.config(text=f"Downloading... {percent:.2f}%")
            root.update_idletasks()
        else:
            status_label.config(text="Downloading... size unknown")
    elif d['status'] == 'finished':
        status_label.config(text="Download completed!")
        play_bell()  # 🔔 Play bell sound
    elif d['status'] == 'error':
        status_label.config(text="Download failed!")

def start_download():
    link = entry.get().strip()
    if not link:
        messagebox.showwarning("Input Error", "Please paste a video link!")
        return

    # Ask user for custom filename
    custom_name = simpledialog.askstring("File Name", "Enter a name for the video file (without extension):")
    if not custom_name:
        custom_name = "%(title)s"  # fallback to video title

    def run_download():
        try:
            ydl_opts = {
                'outtmpl': os.path.join(SAVE_FOLDER, f"{custom_name}.%(ext)s"),
                'format': 'best[ext=mp4]',
                'progress_hooks': [progress_hook]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.download([link])
                # Save to history
                download_history.append(custom_name)
                update_history()
        except Exception as e:
            status_label.config(text="Download failed!")
            messagebox.showerror("Error", str(e))

    threading.Thread(target=run_download, daemon=True).start()

def update_history():
    history_text.delete(0, tk.END)
    for idx, item in enumerate(download_history, start=1):
        history_text.insert(tk.END, f"{idx}. {item}")

def exit_app():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Video Downloader")
root.geometry("600x400")

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

# History section
history_label = tk.Label(root, text="Download History:")
history_label.pack(pady=5)

history_text = tk.Listbox(root, width=80, height=10)
history_text.pack(pady=5)

root.mainloop()