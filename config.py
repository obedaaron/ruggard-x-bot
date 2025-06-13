import tweepy

# HARDCODED CREDENTIALS (TEMPORARY)
BEARER_TOKEN = "your_bearer_token"
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token)
