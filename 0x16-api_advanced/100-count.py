#!/usr/bin/python3
"""More recursive"""
import re
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    # Make request to Reddit API
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params)

    # Check if subreddit exists
    if response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found")
        return
    elif response.status_code == 200:
        # Parse titles of hot articles
        data = response.json()
        for post in data['data']['children']:
            title = post['data']['title'].lower()
            # Count occurrences of each word in word_list
            for word in word_list:
                # Only count full words (not substrings)
                count = len(re.findall(rf"\b{word}\b", title))
                if count > 0:
                    if word in word_count:
                        word_count[word] += count
                    else:
                        word_count[word] = count
        # Check if there are more pages of results
        if data['data']['after'] is not None:
            return count_words(subreddit, word_list, data['data']['after'], word_count)
        else:
            # Print results in descending order by count, and alphabetically if counts are the same
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
            return
    else:
        print("An error occurred while accessing the Reddit API")
        return

