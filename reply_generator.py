# reply_generator.py

from config import api

def post_reply(trigger_tweet_id, analysis_text, trusted_result):
    try:
        reply = f"{analysis_text}\n\n🔎 Trust Check: {trusted_result}"
        api.update_status(status=reply, in_reply_to_status_id=trigger_tweet_id, auto_populate_reply_metadata=True)
        print("✅ Replied successfully!")
    except Exception as e:
        print("❌ Failed to reply:", e)