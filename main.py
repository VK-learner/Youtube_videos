import os
import yt_dlp

save_folder = r"E:\youtube"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

while True:
    link = input("Enter YouTube video link (or type 'exit' to quit): ").strip()
    if link.lower() == "exit":
        print("Exiting program. Goodbye!")
        break

    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_folder, '%(title)s.%(ext)s'),
            'format': 'best[ext=mp4]'  # pick best available single MP4 stream
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        print("Download completed!\n")
    except Exception as e:
        print("Error:", e)