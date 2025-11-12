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

    Returns:
    --------
    True if any keyword in title
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
    try:
        params = {"limit": 25, "raw_json": 1} #Limit to 25 newest posts, amount of daily posts should not exceed this anyway rn
        response = requests.get(REDDIT_API_URL, headers=HEADERS, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        posts = []

        for post in data["data"]["children"]:
            post_data = post["data"]

            if is_turnip_related(post_data["title"]):
                posts.append({
                    "id": post_data["id"],
                    "title": post_data["title"],
                    "url": f"https://reddit.com{post_data["permalink"]}",
                    "author": post_data["author"]
                })
        return posts
    
    except Exception as e:
        logging.error(f"Error fetching Reddit posts: {e}")
        return []

def check_for_new_posts():
    """
    Checks if any of the newest posts havent been seen
    if so: sends one notification per post.

    Returns:
    ---------
    All seen posts.
    """
    seen_posts = load_seen_posts()
    new_posts = fetch_new_posts()

    if not new_posts:
        logging.info("No new posts found")
        return seen_posts
    
    unseen_posts = [post for post in new_posts if post["id"] not in seen_posts]

    if not unseen_posts:
        logging.info("No new unseen posts")
    else:
        logging.info(f"Found {len(unseen_posts)} new posts!")

        for post in unseen_posts:
            logging.info(f"New post: {post["title"]}")
            
            # Send notification via pushover
            send_notification(
                title="New turnip post!",
                message=post["title"],
                url=post["url"]
            )

            # Add post to seen posts
            seen_posts.add(post["id"])

            #Add small delay just in case:
            time.sleep(1)
    return seen_posts

def main():
    """
    Runs checking loop indefinetly
    """
    logging.info("Starting TurnipRadar! Press Ctrl+C to stop.")

    try:
        while True:
            logging.info(f"Checking for new post at {datetime.now()}")

            # Check for new posts and update seen posts if new posts
            seen_posts = check_for_new_posts()
            save_seen_posts(seen_posts)

            logging.info(f"Sleeping for {CHECK_INTERVAL} seconds...")
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        logging.info("TurnipRadar stopped by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    return

if __name__ == "__main__":
    main()