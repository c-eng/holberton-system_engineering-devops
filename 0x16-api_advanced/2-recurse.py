#!/usr/bin/python3
"""returns list of posts of a given subreddit"""


def recurse(subreddit, hot_list=[], after=""):
    """returns list of posts of a given subreddit
    args:
        subreddit (str): subreddit
        hot_list (list:str): list of hots
        after (int): next
    """
    import requests
    dest = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        dest += "?after=" + after
    headers = {"User-Agent": "hbtn API curriculum (Ubuntu)"}
    r = requests.get(dest, headers=headers)
    if r.status_code != 200:
        return None
    try:
        toplist = r.json()['data']['children']
    except:
        return None
    for post in toplist:
        hot_list.append(post.get('data').get('title'))
    lafter = r.json().get('data').get('after')
    if lafter:
        return recurse(subreddit, hot_list, lafter)
    return hot_list
