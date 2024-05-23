This script uses the YouTube API to fetch English subtitles for a given video. 
The script takes a YouTube video ID as an input argument and returns the English subtitles for that video. 
Please make sure you have the YouTube Data API v3 enabled and have obtained the necessary API key.

Arguments:
    video_id (str): The ID of the YouTube video for which to fetch subtitles.
    
Returns:
    str: The English subtitles of the specified video.

HELP:
    What is youtube-id?
        - a query parameter emededded in youtube video urls. For instance, in "https://www.youtube.com/watch?v=q6WlzHLxNKI&list=LL&index=5&t=279s", the string subsequent to v is youtube_id.
