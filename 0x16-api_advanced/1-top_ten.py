#!/usr/bin/python3
"""returns top ten posts of a given subreddit"""


def top_ten(subreddit):
    """returns top ten posts of a given subreddit
    args:
        subreddit (str): subreddit
    """
    import requests
    dest = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python3/requests:htbn API tasks (Ubuntu)"}
    r = requests.get(dest, headers=headers)
    if r.status_code != 200:
        print("None")
        return
    try:
        toplist = r.json()['data']['children']
    except:
        print("None")
        return
    for post in toplist:
        print(post.get('data').get('title'))
