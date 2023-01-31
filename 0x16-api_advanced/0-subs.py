#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers"""
    base_url = "https://api.reddit.com"
    heads = {
            'User-Agent': 'alx _se'
            }
    res = requests.get("{}/r/{}/about".format(base_url,
                       subreddit), headers=heads, allow_redirects=False)
    if (res.status_code == 404):
        return 0
    return res.json().get('data').get('subscribers')
