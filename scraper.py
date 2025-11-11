import requests
import time
import json
import os
import logging
from dotenv import load_dotenv
from datetime import datetime
from notifier import send_notification

load_dotenv()

#Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#Some configs:
YOUR_NAME = os.getenv("YOUR_NAME")
REDDIT_API_URL = "https://www.reddit.com/r/TurnipExchange/new.json"
HEADERS = {"User-Agent": f"TurnipNotifierBot/0.1 by {YOUR_NAME}"}
SEEN_FILE = "seen_posts.json"
CHECK_INTERVAL = 120 #How many seconds between each check

#Set this to false if you do not want to check for posts about daisy mae selling turnips
DO_DAISY_MAE_CHECK = True 

def load_seen_posts():
    """
    Load all seen posts from file

    Returns:
    --------
    
    """

    try:
        if os.path.exists(SEEN_FILE):
            with open(SEEN_FILE, "r") as f:
                return set(json.load(f))
    except Exception as e:
        logging.error(f"Error loading previously seen posts: {e}")
    return set()

def save_seen_posts(seen_posts):
    """
    Save seen posts to file
    """
    try:
        with open(SEEN_FILE, "w") as f:
            json.dump(list(seen_posts), f)
    except Exception as e:
        logging.error(f"Error saving seen posts: {e}")

def is_turnip_related(title):
    """
    Lazy check if post is related to turnips.

    NB! Set DO_DAISY_MAE_CHECK to false if you only want to sell turnips
    """
    title_lower = title.lower()
    keywords = ["turnip", "turnips", "buying", "price", "bells", "nook", "cranny", "timmy", "tommy"]

    if DO_DAISY_MAE_CHECK:
        keywords.append("daisy")
        keywords.append("mae")
        keywords.append("selling")

    return any(keyword in title_lower for keyword in keywords)

def fetch_new_posts():
    """
    Fetches newest Reddit posts using Reddit API.

    Returns:
    --------
    Newest posts or empty list if something goes wrong
    """
    return

def check_for_new_posts():
    """
    Checks if any of the newest posts havent been seen
    if so: sends one notification per post.

    Returns:
    ---------
    All seen posts.
    """
    return

def main():
    """
    Runs checking loop indefinetly
    """
    return

if __name__ == "__main__":
    main()