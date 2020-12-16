#!/usr/bin/python3
""" Count it! """
import requests


def helper(subreddit, word_list, titles, after=None):
    """ recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords """
    urlApi = "https://www.reddit.com/"
    headers = {'User-agent': 'product'}
    endpoint = "r/{}/hot.json?after={}".format(subreddit, after)
    resp = requests.get(endpoint, headers, allow_redirects=False)
    if resp.status_code != 200:
        return None
    if after is None:
        return titles
    data = resp.json().get('data').get('children')
    for datum in data:
        title = datum.get('data').get('title').split()
        for word in set(word_list):
            if word.lower() in [w.lower() for w in title]:
                if titles.get(word):
                    titles[word] += 1
                else:
                    titles[word] = 1
    after = resp.json().get('data').get('after')
    helper(subreddit, word_list, titles, after)
    return titles


def count_words(subreddit, word_list):
    """ function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords """
    titles = helper(subreddit, word_list, {})
    if titles:
        for k, v in sorted(titles.items(), key=lambda value: value[1],
                           reverse=True):
            if v != 0:
                print('{}: {}'.format(k, v))
