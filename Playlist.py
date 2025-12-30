import os
import subprocess

def download_youtube(url, base_folder="D:\\youtube"):
    # Create base folder if not exists
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
        print(f"📂 Created base folder: {base_folder}")

    target_folder = base_folder

    # Detect playlist
    if "playlist?list=" in url:
        playlist_name = input("This looks like a playlist. Enter a name for the playlist folder: ")
        target_folder = os.path.join(base_folder, playlist_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"📂 Created playlist folder: {target_folder}")

    # yt-dlp command
    command = [
        "yt-dlp",
        "-o", os.path.join(target_folder, "%(title)s.%(ext)s"),
        url
    ]

    try:
        subprocess.run(command, check=True)
        print("✅ Download completed!")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    url = input("Paste YouTube playlist or single video link: ")
    download_youtube(url)