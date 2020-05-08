#!/usr/bin/python3
""" Queries and returns a list containing the titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        Recursively queries Reddit API and returns a list containing the
        titles of all hot articles for a given subreddit
    """
    try:
        url = "https://api.reddit.com/r/{}/hot?limit=100".format(subreddit)
        headers = {'user-agent': 'Recurse it'}

        req = requests.get(url, headers=headers, allow_redirects=False,
                           params={'after': after})

        top_json = req.json().get('data').get('children')
        after_val = req.json().get('data').get('after')

        for item in top_json:
            hot_list.append(item.get('data').get('title'))

        if after_val is not None:
            recurse(subreddit, hot_list, after_val)

        return hot_list

    except KeyError:
        return(None)
    except AttributeError:
        return(None)
