# prefect_pipeline.py
import json
import yt_dlp
import pandas as pd
from datetime import datetime
from prefect import flow, task
from prefect.variables import Variable

@task(retries=2, retry_delay_seconds=30)
def extract_youtube_trending_th():
    """Extracts raw metadata from YouTube's trending page for Thailand."""
    # 'yttrending' is the built-in yt-dlp extractor shortcut for trending feeds
    # TH indicates region, and we fetch the flat playlist metadata (no video files download)
    trending_url = "https://www.youtube.com/feed/trending?gl=TH"
    
    ydl_opts = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(trending_url, download=False)
        # Pull entries safely from the extracted dictionary
        videos = info.get('entries', [])
        return videos

@task
def transform_trending_data(raw_videos):
    """Cleans, strips down structural fluff, and structures data into a clean layout."""
    cleaned_list = []
    
    # Process up to top 20 trending videos
    for idx, video in enumerate(raw_videos[:20], start=1):
        cleaned_list.append({
            "Rank": idx,
            "Title": video.get("title"),
            "Channel": video.get("channel"),
            "Views": video.get("view_count", 0),
            "Duration_Sec": video.get("duration", 0),
            "URL": f"https://www.youtube.com/watch?v={video.get('id')}",
            "Extracted_At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
    return cleaned_list

@task
def load_to_prefect_cloud(cleaned_data):
    """Pushes the JSON array straight into a Prefect Cloud workspace variable."""
    # Converts data to an easy-to-transport string format
    json_string = json.dumps(cleaned_data)
    
    # Creates or overwrites a global variable named 'thailand_yt_trending'
    Variable.set(name="thailand_yt_trending", value=json_string, overwrite=True)
    print("Successfully updated trend data in Prefect Cloud!")

@flow(name="YouTube Thailand Trends ETL")
def youtube_etl_flow():
    raw_data = extract_youtube_trending_th()
    processed_data = transform_trending_data(raw_data)
    load_to_prefect_cloud(processed_data)

if __name__ == "__main__":
    # Log in to prefect cloud locally via command line first: `prefect cloud login`
    youtube_etl_flow()
