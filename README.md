# TurnipRadar
TurnipRadar is a python app that scrapes r/TurnipExchange for any new posts, and sends a notification to your phone with a link to the reddit post, so that you can queue up to sell turnips as fast as possible. 

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
- Add support for more than one subreddit
