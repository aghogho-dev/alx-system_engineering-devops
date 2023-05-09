#!/usr/bin/python3
"""Get the number of subs"""
import requests

def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    try:
        return res.json().get("data").get("subscribers")
    except requests.exceptions.JSONDecodeError:
        return 0
