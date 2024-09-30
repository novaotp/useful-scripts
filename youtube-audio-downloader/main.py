from pathlib import Path
from youtube import Youtube


def output_path() -> Path:
    """
    Returns the output path where converted audio files will be saved.

    :return: The output path as a Path object
    """
    script_dir = Path(__file__).parent

    return script_dir / "output"


def main():
    youtube = Youtube(output_path=output_path())

    url = input("Enter the YouTube video URL: ")
    youtube.download(url, format="mp3")


if __name__ == "__main__":
    main()
