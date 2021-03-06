#!/usr/bin/python3
""" Finds the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
        Print the titles of the first 10 hot posts listed for a given subreddit
    """

    try:
        url = "https://api.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {'user-agent': 'Top Ten'}
        req = requests.get(url, headers=headers, allow_redirects=False)
        top_json = req.json().get('data').get('children')

        if req.status_code == 200:
            for top in top_json:
                print(top.get('data').get('title'))

    except KeyError:
        print(None)
    except AttributeError:
        print(None)


if __name__ == '__main__':
    top_ten(subreddit)
