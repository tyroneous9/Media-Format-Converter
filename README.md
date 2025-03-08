# Video & Audio Converter

A Python-based YouTube Downloader that allows users to convert online videos into audio and video formats with an intuitive Tkinter UI.

## Features

### User Interface
- Simple Tkinter-based UI for selecting formats and output directories.
- Users can enter multiple YouTube links at once.

### Format Conversion
- Supports audio (m4a) and video (mp4) downloads.
- Uses yt-dlp for efficient downloading.

### Automated Error Handling
- Detects and handles invalid URLs.
- Warns users of network failures or unsupported formats.

### Export Directory Selection
- Users can choose custom output directories.

### Multi-Threaded Downloads & Batch Processing
- Multiple downloads run in parallel for faster conversions.
- Uses multi-threading to prevent UI freezing.

## Installation

### 1. Install Dependencies
Ensure you have Python 3 installed, then install the required libraries:

```
pip install yt-dlp tk
```

### 2. Run the Application

python dl_multithreaded.py

## How to Use

1. Enter YouTube video URLs into the text box.
2. Select a format (Audio or Video).
3. Choose an output directory (default: Downloads).
4. Click "Convert" to start the download.
5. Wait for completion messages while multiple downloads run in parallel.

## Future Improvements

- Support for more formats (e.g., WAV, AVI).
- Progress bar integration to track download progress.
- Improved error recovery for failed downloads.
- Download queue management for better user control.
