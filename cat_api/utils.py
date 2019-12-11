import requests
import json
import urllib.request


def _get(response):
    if response == None:
        res = requests.get('https://api.thecatapi.com/v1/images/search?format=json')
        if res.status_code == 200:
            return res.json()[0]["url"]
        else:
            return res
    else:
        res = requests.get('https://api.thecatapi.com/v1/breeds/')
        if res.status_code == 200:
            return res.json()
        else:
            return res

