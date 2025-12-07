# TurnipRadar
TurnipRadar is a python app that uses the Reddit API to check r/TurnipExchange for any new posts related to selling or buying turnips. It sends a notification to your phone with a link to the reddit post, so that you can queue up to sell turnips as fast as possible. 

## How to run:
Requires python to run!

Rename .env.example to .env, which will look like this:
```bash
USER_PUSHOVER_KEY = "Your pushover key goes here"
API_TOKEN = "Your pushover api token goes here"
YOUR_NAME = "Your name/username/nickname goes here"

# How many seconds between each scrape
CHECK_INTERVAL=120

# Set this to true if you also want to check for posts about Daisy Mae selling turnips
DO_DAISY_MAE_CHECK=True

# Set this to true if you only want to send notifications if post age is under MAX_POST_AGE minutes
ONLY_SEND_NOTIFICATION_IF_REALLY_NEW=True
MAX_POST_AGE=60

# Name of the file containing your seen posts
SEEN_FILE=seen_posts.json
```

Then you run this to give the startup script execution permissions:
```bash
chmod +x start.sh
```

Then you can run the app by doing:
```bash
./start.sh
```

## TODO:
- [ ] Add support for more than one subreddit
- [x] Add config file with user stuff: `DO_DAISY_MAE_CHECK`, `ONLY_SEND_NOTIFICATION_IF_REALLY_NEW` and etc.
- [ ] Add possibility to automatically comment on new reddit posts.
- [x] bug: posts are not appended if they are skipped, so they will be checked upon restart even if they were skipped. Solve by moving `is_post_recent-check` to `check_for_new_posts`
- [ ] bug: If a post changes title notification is sent again
