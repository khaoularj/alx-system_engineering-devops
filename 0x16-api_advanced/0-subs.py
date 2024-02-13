#!/usr/bin/python3
"""this function that queries the Reddit API
and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    If not a valid subreddit, return 0"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        n_subscribers = data.get("subscribers")
        return n_subscribers
    else:
        return 0


if __name__ == '__main__':
    print(number_of_subscribers(subreddit))
