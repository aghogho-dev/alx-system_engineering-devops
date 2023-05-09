#!/usr/bin/python3
"""Get the number of subs"""
import json
import urllib.request

def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/0.0.1"}

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            dt = json.loads(response.read().decode())
            return dt['data']['subscribers']
    except Exception:
        return 0

