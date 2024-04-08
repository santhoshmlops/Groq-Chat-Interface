# Importing necessary modules
from langchain_community.document_loaders import YoutubeLoader

# Function to extract text from YouTube videos
def get_youtube_text(URLS):
    # Initializing YoutubeLoader with the provided YouTube URLs
    loader = YoutubeLoader.from_youtube_url(URLS, add_video_info=False,
                                            language=["en", "id"],
                                            translation="en")
    
    # Loading data from the YouTube videos
    data = loader.load()   
    
    return data