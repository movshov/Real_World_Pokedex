import requests
import json
import urllib.request

url = 'https://api.thecatapi.com/v1/images/search?format=json'


def _get():
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return res



#import urllib.request, json 
#with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
        #data = json.loads(url.read().decode())
            #print(data)
