from multiprocessing import Pool, cpu_count
import os
import sys
import datetime
from moviepy.editor import VideoFileClip
from deep_translator import GoogleTranslator
import subprocess
import torch
import whisper


# Ensure all CPU cores are used
torch.set_num_threads(cpu_count() - 2)

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

# Check if ffmpeg is installed
def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log("FFmpeg is installed and accessible.")
    except subprocess.CalledProcessError:
        log("FFmpeg is not installed or not accessible. Please install FFmpeg and add it to your PATH.")
        sys.exit(1)

# Generate SRT file from transcriptions
def generate_srt(transcriptions, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, (start, end, text) in enumerate(transcriptions):
            f.write(f"{i + 1}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")

# Format timestamp for SRT
def format_timestamp(seconds):
    return f"{int(seconds // 3600):02}:{int((seconds % 3600) // 60):02}:{int(seconds % 60):02},{int(seconds * 1000) % 1000:03}"

# Transcribe audio to English
def transcribe_audio(audio_file):
    log(f"Loading Whisper model...")
    model = whisper.load_model("large-v2")
    log(f"Transcribing audio from {audio_file}...")
    result = model.transcribe(audio_file)
    log(f"Audio transcribed successfully.")

    transcriptions = []
    for i, segment in enumerate(result['segments']):
        start_time = format_timestamp(segment['start'])
        end_time = format_timestamp(segment['end'])
        transcriptions.append((start_time, end_time, segment['text']))
        log(f"Segment {i + 1}: Transcribed text: {segment['text']}")

    return transcriptions

# Translate English transcriptions to Portuguese (Brazilian)
def translate_to_portuguese(transcriptions):
    translator = GoogleTranslator(source='en', target='pt-br')
    log("Starting translation of transcriptions to Portuguese (Brazilian)...")

    transcriptions_pt = []
    for i, (start, end, text) in enumerate(transcriptions):
        try:
            translated_text = translator.translate(text)
            transcriptions_pt.append((start, end, translated_text))
            log(f"Segment {i + 1}: Translated text: {translated_text}")
        except Exception as e:
            log(f"Segment {i + 1}: Translation error: {e}")
            transcriptions_pt.append((start, end, text))

    log("Translation to Portuguese (Brazilian) completed.")
    return transcriptions_pt

# Extract audio from video
def extract_audio(video_file):
    audio_file = os.path.splitext(video_file)[0] + ".mp3"
    log(f"Extracting audio from {video_file}...")
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(audio_file)
    clip.close()
    log(f"Audio file created: {audio_file}")
    return audio_file

# Clean up temporary files
def clean_up(file):
    if os.path.exists(file):
        log(f"Cleaning up file: {file}")
        os.remove(file)

# Main function to process video file
def main(video_file):
    if not os.path.exists(video_file):
        log(f"File not found: {video_file}")
        sys.exit(1)

    check_ffmpeg()

    audio_file = extract_audio(video_file)

    try:
        # Transcribe to English
        transcriptions_en = transcribe_audio(audio_file)
        base_name = os.path.splitext(video_file)[0]
        generate_srt(transcriptions_en, f"{base_name}.en.srt")

        # Translate to Portuguese (Brazilian)
        transcriptions_pt = translate_to_portuguese(transcriptions_en)
        generate_srt(transcriptions_pt, f"{base_name}.pt-BR.srt")

        log("Subtitles generated successfully!")
    except Exception as e:
        log(f"An error occurred: {str(e)}")
        log("Traceback:")
        import traceback
        log(traceback.format_exc())
    finally:
        clean_up(audio_file)

# Execute script if run directly
if __name__ == "__main__":
    if len(sys.argv) < 2:
        log("Usage: python generate_subtitles.py <video_file>")
        sys.exit(1)

    video_file = " ".join(sys.argv[1:])
    main(video_file)


