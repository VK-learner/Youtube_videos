# YouTube Video Downloader

A simple Python desktop application built with **Tkinter** and **yt-dlp** to download YouTube videos with real-time progress tracking, custom file naming, and download history.

## Features

- **Simple GUI**: Clean and intuitive interface built with Tkinter
- **Real-time Progress**: Displays download percentage as the video downloads
- **Custom File Naming**: Prompts for a custom filename before each download
- **Download History**: Tracks all downloaded files within the session
- **Bell Notification**: Plays a sound when download completes
- **Robust Format Selection**: Tries best available MP4 with fallbacks
- **Threading**: Non-blocking downloads prevent GUI freezing
- **Standalone Executable**: Can be packaged as a `.exe` using PyInstaller

## Project Structure

```
Youtube_videos/
├── app2.py         # Main application (current version)
├── app2.spec       # PyInstaller specification file
├── icon.ico        # Application icon
├── dist/           # Compiled executable files
└── build/          # Build artifacts
```

## Requirements

- Python 3.7 or higher
- `tkinter` (comes with Python)
- `yt-dlp` — YouTube downloader library
- `ffmpeg` — Required for merging video and audio streams

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/VK-learner/Youtube_videos.git
   cd Youtube_videos
   ```

2. Install required dependencies:
   ```bash
   pip install yt-dlp
   ```

3. Install ffmpeg and add it to PATH:
   - Download from https://ffmpeg.org/download.html
   - Add the `bin/` folder to your system PATH

## Usage

Run the application:
```bash
python app2.py
```

### How to Download

1. Paste a YouTube video URL in the text field
2. Click the **Download** button
3. Enter a custom filename when prompted (or leave blank to use the video title)
4. Watch the real-time progress percentage
5. A bell sound plays when the download completes
6. Videos are saved to `E:\youtube` by default

## Configuration

Change the save location by modifying `SAVE_FOLDER` in `app2.py`:

```python
SAVE_FOLDER = r"E:\youtube"  # Change this path
```

## Creating a Standalone Executable

```bash
pip install pyinstaller
pyinstaller app2.spec
```

The executable will be in the `dist/` folder.

## Technical Details

- **Format Selection**: `bestvideo[ext=mp4]+bestaudio[ext=m4a]` with fallbacks — uses ffmpeg to merge streams
- **Player Clients**: Forces `web` and `android` clients via `extractor_args` to work around YouTube's SABR streaming restrictions
- **Progress Tracking**: Uses yt-dlp's `progress_hook` callback
- **Threading**: Downloads run in a daemon thread to keep UI responsive
- **Output Format**: Always merged to `.mp4`

## Troubleshooting

**Issue**: `Module not found` error
- **Solution**: `pip install yt-dlp`

**Issue**: Fragments skipped / empty file downloaded
- **Solution**: Update yt-dlp (`pip install -U yt-dlp`) and ensure ffmpeg is on PATH

**Issue**: `No supported JavaScript runtime` warning
- **Solution**: Install Node.js from https://nodejs.org — yt-dlp uses it for YouTube extraction

**Issue**: Permission denied when saving
- **Solution**: Ensure the save folder exists and you have write permissions

## Future Enhancements

- [ ] Playlist support
- [ ] Audio-only download option
- [ ] Format selection dropdown
- [ ] Download queue management
- [ ] Video thumbnail preview
- [ ] Persistent download history across sessions

## License

MIT License

## Author

**VK-learner** — Built as a practical utility for downloading YouTube videos