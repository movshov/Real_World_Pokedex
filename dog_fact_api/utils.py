
# using the dog Facts API - https://dog-api.kinduff.com/api/facts

import requests

base_url = 'https://dog-api.kinduff.com/api'

def _get(resource='facts'):
    """Sends a GET request to the provided resource and returns the 'facts' data if it exitsts."""
    url = '{}{}'.format(base_url, resource)
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()['facts']
    else:
        return res

