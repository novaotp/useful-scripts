import os
from pathlib import Path
import subprocess


class Youtube:
    def __init__(self, output_path: str | Path = "./output"):
        """
        Initializes a new instance of the Youtube class.

        :param output_path: The path where the converted audio file will be saved
        :return: An instance of the Youtube class
        """
        self.output_path = output_path

    def download(self, youtube_url: str, format: str = "mp3") -> None:
        """
        Downloads a YouTube video as audio and converts it to the specified format.

        :param youtube_url: The URL of the YouTube video to download
        :param format: The format to convert the audio to, defaults to "mp3"
        """
        try:
            print(f"Downloading video from URL: {youtube_url}")
            command = [
                "yt-dlp",
                "-x",  # Extract audio
                "--no-playlist",  # Only download the video and not the whole playlist
                "--audio-format",
                format,  # Convert to format
                "-o",
                os.path.join(
                    self.output_path, "%(title)s.%(ext)s"
                ),  # Output file format
                youtube_url,
            ]
            subprocess.run(command, check=True)
            print(f"Download and conversion completed successfully!")

        except subprocess.CalledProcessError as e:
            print(f"Error during download or conversion: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")
