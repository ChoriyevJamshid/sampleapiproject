import pprint

import httpx
import requests

base_url = 'http://127.0.0.1:8000/api/v1/'

# def get_categories():
#     url = base_url + 'categories/'
#     auth = ('admin', 'admin')
#     response = httpx.get(url=url, auth=auth)
#
#     print(response.status_code)
#     if response.status_code == 200:
#         categories = response.json()
#         pprint.pprint(categories)
# get_categories()

def get_posts():
    url = base_url + 'posts/'
    auth = ('admin', 'admin')
    response = httpx.get(url=url, auth=auth)

    print(response.status_code)
    if response.status_code == 200:
        categories = response.json()
        pprint.pprint(categories)


get_posts()

