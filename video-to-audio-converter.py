import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def convert_video_to_audio(video_path):
    # Start
    print("Starting video to audio conversion process...")

    # Open Python Video
    try:
        video = VideoFileClip(video_path)
    except Exception as e:
        print(f"Error opening video file: {e}")
        return

    # Check File Format
    _, file_extension = os.path.splitext(video_path)
    
    # Valid Format?
    if file_extension.lower() == '.mp4':
        print("Valid format detected: mp4")
        
        # Extract Audio
        print("Extracting audio...")
        audio = video.audio
        
        # Convert to mp3
        print("Converting to mp3...")
        output_path = os.path.splitext(video_path)[0] + ".mp3"
        audio.write_audiofile(output_path)
        
        # Save mp3 File
        print(f"Audio saved as: {output_path}")
        
        # Close video file
        video.close()
        
        print("Conversion complete!")
    else:
        # Invalid Format
        print(f"Invalid format: {file_extension}. Only .mp4 files are supported.")

    # End
    print("Process ended.")

# Example usage
if __name__ == "__main__":
    video_file = input("Enter the path to your video file: ")
    convert_video_to_audio(video_file)
