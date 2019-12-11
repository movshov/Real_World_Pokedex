# Building off Bar's formatting
# using the Cat Facts API - catfact.ninja

import requests

base_url = 'https://catfact.ninja/'

def _get(resource='fact'):
    """Sends a GET request to the provided resource and returns the 'message' data if it exitsts."""
    url = '{}{}'.format(base_url, resource)
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['fact']
    else:
        return res

