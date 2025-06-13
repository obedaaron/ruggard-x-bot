# 🕵️‍♂️ RugGuard X Bot

A Twitter/X bot built for the **@SuperteamDAO x @projectrugguard** bounty.

This bot monitors replies for the phrase **"riddle me this"**, analyzes the **original tweet’s author**, and replies with a **trustworthiness report** based on:

- 🔹 Account age  
- 🔹 Follower/following ratio  
- 🔹 Bio content  
- 🔹 Engagement metrics  
- 🔹 Presence in the trusted follower network  

Built using Python and the `tweepy` library.

---

## 🚀 How It Works

1. **Listens** for replies containing `"riddle me this"`.
2. **Identifies** the author of the tweet being replied to.
3. **Analyzes** trust signals using public data and follower trust checks.
4. **Replies** to the trigger comment with a summary of the author's trustworthiness.

---

## 🔧 Setup Instructions

> Make sure you have Python 3.8+ installed.

### 1. Clone the repository
```bash
git clone https://github.com/obedaaron/ruggard-x-bot.git
cd ruggard-x-bot


2. Install Dependencies
pip install -r requirements.txt
This includes: tweepy, requests, datetime, etc.

3. Set Your Twitter API Keys
Open the config.py file and paste in your credentials like this:
import tweepy

# Twitter Developer Credentials
BEARER_TOKEN = "your_bearer_token"
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

4. Run the Bot
python main.py

💻 Replit Compatibility
This bot runs perfectly on Replit.com:

Upload the code files

Paste your credentials into config.py

Click Run
