#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return number of hot topics in a subreddit"""
    base_url = "https://api.reddit.com"
    heads = {
            'User-Agent': 'alx_se'
            }
    para = {
            "after": after,
            "count": count
            }
    res = requests.get("{}/r/{}/hot".format(base_url,
                       subreddit), headers=heads,
                       params=para, allow_redirects=False)
    if (res.status_code == 404):
        return None
    data = res.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    children = res.json().get('data').get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))
    if (after is not None):
        recurse(subreddit, hot_list, after, count)

    return hot_list
