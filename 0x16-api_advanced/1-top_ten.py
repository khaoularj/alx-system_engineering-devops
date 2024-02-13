#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data").get("children")
        F_10_posts = "\n".join(post.get("data").get("title") for post in data)
        print(F_10_posts)
    else:
        print("None")
        return
