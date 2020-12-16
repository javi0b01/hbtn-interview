#!/usr/bin/python3
""" Count it! """
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """ function that queries the Reddit API, parses the title of all hot
    articles, and prints a sorted count of given keywords """
    try:
        endpoint = "https://www.reddit.com/r/{}/hot.json?after={}"
        headers = {'User-Agent': 'custom'}
        r = requests.get(endpoint.format(subreddit, after), headers, allow_redirects=False)
        if after is None:
            dict = {}
            for word in word_list:
                for hot_word in hot_list:
                    if word == hot_word:
                        if word not in dict:
                            dict[word] = 1
                        else:
                            dict[word] += 1
            for word in sorted(dict, key=dict.get, reverse=True):
                if dict[word]:
                    print('{}: {}'.format(word, dict[word]))
            return hot_list
        for thread in r.json().get('data').get('children'):
            hot_list += thread.get('data').get('title').lower().split()
        after = r.json().get('data').get('after')
        count_words(subreddit, word_list, hot_list, after)
        return hot_list
    except:
        return None
