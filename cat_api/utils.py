import requests
import json
import urllib.request

url = 'https://api.thecatapi.com/v1/images/search?format=json'


def _get():
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()[0]["url"]
    else:
        return res

