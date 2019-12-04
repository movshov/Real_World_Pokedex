# Code is taken from https://github.com/joebeachjoebeach/dog-api/blob/master/dog_api/utils.py
# all credit goes to the original creator. 

import requests

base_url = 'https://dog.ceo/api/'

def _get(resource):
    """Sends a GET request to the provided resource and returns the 'message' data if it exitsts."""
    url = '{0}{1}'.format(base_url, resource)
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['message']
    else:
        return res

