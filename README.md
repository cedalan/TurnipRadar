# TurnipRadar
TurnipRadar is a python app that uses the Reddit API to check r/TurnipExchange for any new posts related to selling or buying turnips. It sends a notification to your phone with a link to the reddit post, so that you can queue up to sell turnips as fast as possible. 

## How to run:
Requires python to run!

Create a .env file containing info like this:
```bash
USER_PUSHOVER_KEY = "Your pushover key goes here"
API_TOKEN = "Your pushover api token goes here"
YOUR_NAME = "Your name/username/nickname goes here"
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
- [ ] Add config file with user stuff: `DO_DAISY_MAE_CHECK`, `ONLY_SEND_NOTIFICATION_IF_REALLY_NEW` and etc.
- [x] bug: posts are not appended if they are skipped, so they will be checked upon restart even if they were skipped. Solve by moving `is_post_recent-check` to `check_for_new_posts`
- [ ] bug: If a post changes title notification is sent again
