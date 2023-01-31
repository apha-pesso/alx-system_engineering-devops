#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def top_ten(subreddit):
    """Return number of subscribers"""
    base_url = "https://api.reddit.com"
    heads = {
            'User-Agent': 'alx_se'
            }
    para = {
            "limit": 10
            }
    res = requests.get("{}/r/{}/hot".format(base_url,
                       subreddit), headers=heads,
                       params=para, allow_redirects=False)
    if (res.status_code == 404):
        return print(None)
    children = res.json().get('data').get('children')
    title = []
    for child in children:
        title.append(child.get('data').get('title'))
    print("\n".join(title))
