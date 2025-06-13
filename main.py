# main.py

import tweepy
import time
import re
from config import client, api
from analyze_account import analyze_account
from trusted_check import check_trusted
from reply_generator import post_reply

TRIGGER_PHRASE = "riddle me this"
MENTIONED_USERNAME = "projectruggaurd"  # Change if different
CHECK_INTERVAL = 60  # seconds

processed_tweets = set()

def find_trigger_mentions():
    print("Checking for mentions...")
    mentions = client.get_users_mentions(id=api.me().id, max_results=10)
    if mentions.data is None:
        return []

    new_triggers = []

    for tweet in mentions.data:
        if tweet.id in processed_tweets:
            continue

        text = tweet.text.lower()
        if TRIGGER_PHRASE in text and f"@{MENTIONED_USERNAME}" in text:
            # Get the original tweet this is replying to
            if hasattr(tweet, 'referenced_tweets') and tweet.referenced_tweets:
                original_tweet_id = tweet.referenced_tweets[0].id
                original = client.get_tweet(original_tweet_id, expansions="author_id")
                if original and original.includes and "users" in original.includes:
                    original_author = original.includes["users"][0]
                    new_triggers.append({
                        "trigger_tweet_id": tweet.id,
                        "trigger_user": tweet.author_id,
                        "original_author_id": original_author.id,
                        "original_author_username": original_author.username
                    })
                    processed_tweets.add(tweet.id)
    return new_triggers


def main():
    while True:
        try:
            triggers = find_trigger_mentions()
            for trigger in triggers:
                print(f"🔍 Analyzing @{trigger['original_author_username']}...")

                analysis = analyze_account(trigger["original_author_id"])
                trusted_result = check_trusted(trigger["original_author_id"])
                post_reply(trigger["trigger_tweet_id"], analysis, trusted_result)

        except Exception as e:
            print("Error:", e)

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()