# MP4 → MP3 Converter

A simple and user-friendly desktop application for converting MP4 video files to MP3 audio format. Built with Python and Tkinter, featuring a modern dark-themed interface.

## Features

- 🎬 Convert MP4 videos to MP3 audio files
- 📁 Batch conversion support - convert multiple files at once
- 🎨 Modern dark-themed user interface
- 📊 Progress bar to track conversion status
- 📂 Custom output folder selection
- ⚡ Threaded conversion for non-blocking UI

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `moviepy`
  - `tkinter` (usually included with Python)

## Installation

1. Clone or download this repository

2. Install the required dependencies:
   ```bash
   pip install moviepy
   ```

   **Note:** MoviePy may also require FFmpeg to be installed on your system. On Windows, you can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

3. Run the application:
   ```bash
   python mp3_converter.py
   ```

## Usage

1. **Select MP4 Files**: Click the "Select MP4 Files" button to choose one or more MP4 video files you want to convert.

2. **Select Output Folder**: Click the "Select Output Folder" button to choose where you want to save the converted MP3 files.

3. **Convert**: Click the "Convert to MP3" button to start the conversion process.

4. **Monitor Progress**: Watch the progress bar and status label to track the conversion progress.

5. **Completion**: Once all files are converted, you'll see a completion message. The MP3 files will be saved in your selected output folder with the same names as the original video files.

## Notes

- The converted MP3 files will have the same filename as the original MP4 files (with .mp3 extension)
- If a video file has no audio track, an error message will be displayed
- The conversion process runs in a separate thread, so the UI remains responsive during conversion

## Troubleshooting

- **FFmpeg not found**: If you encounter FFmpeg-related errors, make sure FFmpeg is installed and accessible from your system PATH.
- **No audio found**: Some video files may not contain audio tracks. The converter will skip these files and display an error.
- **Import errors**: Make sure all required packages are installed using `pip install moviepy`

## License

This project is open source and available for personal and educational use.

