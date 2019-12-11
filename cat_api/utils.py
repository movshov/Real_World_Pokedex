import requests
import json
import urllib.request

# return an image based on cat breed name.
base_url = 'https://api.thecatapi.com/v1/images/search?q='

def _get(resource):
    # return random image of any cat.
    if resource == None:
        res = requests.get('https://api.thecatapi.com/v1/images/search?format=json')
        if res.status_code == 200:
            return res.json()[0]["url"]
        else:
            return res

    # return all cat breeds.
    elif resource == 'swiggty_swaggity':
        res = requests.get('https://api.thecatapi.com/v1/breeds/')
        if res.status_code == 200:
            return res.json()
        else:
            return res

    # return one url of an image of a specific breed.
    else:
        # set up url with the breed we want to search for. 
        url = '{0}{1}'.format(base_url, resource)
        # print("resource is: \n", resource)
        # call a get request on the url we just made. 
        res = requests.get(url)
        # if the request was successfull return the json package. 
        if res.status_code == 200:
            # print("json is: \n", res.json())
            return res.json()[0]['url']
        else:
            return res


