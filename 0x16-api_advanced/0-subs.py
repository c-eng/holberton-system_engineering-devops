#!/usr/bin/python3
"""returns number of subscribers for a given reddit sub"""


def number_of_subscribers(subreddit):
    """returns number of subscribers for a given reddit sub
    args:
        subreddit (str): subreddit
    """
    import requests
    dest = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"User-Agent": "python3/requests (Ubuntu)"}
    r = requests.get(dest, headers=headers)
    if (r.status_code != 200 or 'data' not in r.json().keys() or
        'subscribers' not in r.json().get('data').keys()):  # noqa
        return 0
    return r.json().get('data').get('subscribers')
