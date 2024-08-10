# Subtitle Generator

This project is a Python script that extracts audio from videos, transcribes the audio to English using the Whisper model from OpenAI, and translates the transcriptions to Brazilian Portuguese (pt-BR). The script generates SRT files containing subtitles in both languages.

## Prerequisites

Before running the script, ensure that the following software and packages are installed:

1. **Python 3.9** or higher
2. **FFmpeg** (for audio and video manipulation)
3. Python packages listed in the `requirements.txt` file

### FFmpeg Installation

To install FFmpeg, follow the appropriate instructions for your operating system and add the path to the `ffmpeg` executable to your system PATH.

- [Instructions for installing FFmpeg](https://ffmpeg.org/download.html)

## Environment Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/luizfgemi/generate_subtitles.git
    cd generate_subtitles
    ```

2. Install the required dependencies:

    ```bash
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```

## How to Use

### Using the Python Script

To generate subtitles, run the `generate_subtitles.py` script with the video file as an argument:

```bash
python generate_subtitles.py your_video.mp4
```

The script will:

1. Extract audio from the video.
2. Transcribe the audio to English.
3. Translate the transcriptions to Brazilian Portuguese.
4. Generate two SRT files (`your_video.en.srt` and `your_video.pt-BR.srt`) with subtitles in English and Portuguese, respectively.

### Using the `.bat` Script

You can also use the `run_generate_subtitles.bat` script to simplify execution on Windows. Simply drag and drop the video file onto the `.bat` script or run it directly by passing the video path as an argument.

```bash
run_generate_subtitles.bat your_video.mp4
```

### Verifying and Installing Dependencies

To ensure all dependencies are installed correctly, you can use the `install_dependencies.bat` script. This script checks if Python and FFmpeg are installed and then installs the necessary Python packages.

```bash
install_dependencies.bat
```

## Logs

The script generates logs in the console that help track the progress and identify any errors during execution.

## Cleaning Up Temporary Files

At the end of execution, the script automatically removes the extracted audio file from the video.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Feel free to open issues and pull requests for improvements or bug fixes.

## Contact

For questions or suggestions, feel free to contact at `your-email@domain.com`.
