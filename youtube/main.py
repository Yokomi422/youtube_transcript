"""
This script uses the YouTube API to fetch English subtitles for a given video. 
The script takes a YouTube video ID as an input argument and returns the English subtitles for that video. 
Please make sure you have the YouTube Data API v3 enabled and have obtained the necessary API key.

Arguments:
    video_id (str): The ID of the YouTube video for which to fetch subtitles.
    
Returns:
    str: The English subtitles of the specified video.

HELP:
    What is youtube-id?
        - A query parameter embedded in YouTube video URLs. For instance, in "https://www.youtube.com/watch?v=q6WlzHLxNKI&list=LL&index=5&t=279s", 
          the string subsequent to 'v' is the youtube_id.

Usage:
    python script_name.py <youtube_id>
"""

import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def fetch_subtitles(video_id):
    """
    Fetches English subtitles for a given YouTube video ID.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        str: The formatted English subtitles.
    """
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    formatter = TextFormatter()
    formatted_transcript = formatter.format_transcript(transcript)
    return formatted_transcript

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <youtube_id>")
        sys.exit(1)

    video_id = sys.argv[1]
    try:
        subtitles = fetch_subtitles(video_id)
        print(subtitles)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
