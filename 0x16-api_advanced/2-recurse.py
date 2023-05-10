#!/usr/bin/python3
"""Recursive"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursive to get hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 100, "after": after, "count": count}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    try:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
    except requests.exceptions.JSONDecodeError:
        return None
    return hot_list
