#!/usr/bin/python3
"""Recursive"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive to get hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    try:
        data = response.json().get("data")
        if not data or not data.get("children"):
            return hot_list
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))
        after = data.get("after")
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except requests.exceptions.JSONDecodeError:
        return None
