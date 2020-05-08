#!/usr/bin/python3
""" Finds the number of subscribers for a given subbreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries Reddit and returns the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'How many subs'}

    req = requests.get(url, headers=headers, allow_redirects=False)

    return req.json().get('data').get('subscribers')\
        if req.status_code is 200 else 0


if __name__ == '__main__':
    number_of_subscribers(subreddit)
