#!/usr/bin/python3
"""Recursive"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    url = f"https://www.reddit.com/r/{subreddit}/hot
