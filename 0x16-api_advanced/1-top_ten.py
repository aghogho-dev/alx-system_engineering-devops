#!/usr/bin/python3
"""Get Top 10"""
import requests


def top_ten(subreddit):
    """Get Top 10"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
    try:
        results = response.json().get("data")
        [print(child.get("data").get("title")) for child in results.get("children")]
    except requests.exceptions.JSONDecodeError:
        print(None)
    return
