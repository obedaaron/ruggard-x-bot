# analyze_account.py

import tweepy
from config import client
from datetime import datetime

def analyze_account(user_id):
    try:
        user = client.get_user(id=user_id, user_fields=["created_at", "description", "public_metrics"])
        if not user.data:
            return "Could not fetch user data."

        u = user.data
        metrics = u.public_metrics

        # Account Age
        created_at = u.created_at
        age_days = (datetime.utcnow() - created_at).days
        age_str = f"{age_days // 365}y {(age_days % 365) // 30}mo"

        # Follower / Following ratio
        followers = metrics['followers_count']
        following = metrics['following_count']
        ratio = round(followers / following, 2) if following > 0 else "N/A"

        # Bio analysis
        bio = u.description or ""
        bio_score = "🟢" if len(bio) > 10 else "🔴"

        report = f"""
📊 **Trust Report for @{u.username}**

🕐 Account Age: {age_str}
👥 Followers: {followers} | Following: {following} | Ratio: {ratio}
📜 Bio: {bio_score} ({'present' if len(bio) > 10 else 'missing'})
        """.strip()

        return report

    except Exception as e:
        return f"Error during analysis: {e}"
