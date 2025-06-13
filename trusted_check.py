# trusted_check.py

import requests
from config import client

TRUST_LIST_URL = "https://raw.githubusercontent.com/devsyrem/turst-list/main/list"

def check_trusted(user_id):
    try:
        resp = requests.get(TRUST_LIST_URL)
        trust_list = [line.strip().lower() for line in resp.text.splitlines() if line.strip()]
        
        # Get followers (max 1000)
        follows = client.get_users_followers(id=user_id, max_results=1000)
        if not follows.data:
            return "🔴 Not followed by any trusted accounts."

        followers_usernames = [f.username.lower() for f in follows.data]

        count = sum(1 for user in trust_list if user in followers_usernames)
        if count >= 3:
            return f"✅ Followed by {count} trusted accounts. Looks reliable!"
        elif count == 2:
            return f"🟡 Followed by 2 trusted accounts. Decent signal."
        else:
            return f"🔴 Only {count} trusted follows. Be cautious."

    except Exception as e:
        return f"Error checking trusted status: {e}"
