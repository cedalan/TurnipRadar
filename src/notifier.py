import requests
import os
from dotenv import load_dotenv

PUSHOVER_API_URL = "https://api.pushover.net/1/messages.json"

load_dotenv()

USER_PUSHOVER_KEY = os.getenv("USER_PUSHOVER_KEY")
API_TOKEN = os.getenv("API_TOKEN")

def send_notification(title: str, message: str, url: str = None):
    """
    Sends a notification with pushover given some user key and api token.

    Params:
    -------
    title: Pushover notificaiton title
    message: Pushover message
    url: url of reddit post
    """
    if not USER_PUSHOVER_KEY or not API_TOKEN:
        raise ValueError("Missing Pushover credentials! Make sure both your pushover key and api token exists in .env")
    
    payload = {
        "token": API_TOKEN,
        "user": USER_PUSHOVER_KEY,
        "title": title,
        "message": message
    }

    if url:
        payload["url"] = url
        payload["url_title"] = "View reddit post"

    response = requests.post(PUSHOVER_API_URL, data=payload)

    if response.status_code != 200:
        print(f"Failed to send notification! Reponse: {response.text}")
    else:
        print("Notification sent successfully!")