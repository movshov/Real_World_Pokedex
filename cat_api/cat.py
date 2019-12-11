from .utils import _get

def random_image(response=None):
    """Gets a random image of a cat. Returns a string of url image link."""
    return _get(response)

def master_breeds():
    """Gets all breeds from cat api. Returns a dict of json objects."""
    return _get('swiggty_swaggity')

def breeds(breed):
    """Gets a random image of a cat based on a breed. Returns a url of an image."""
    if not isinstance(breed,str):
        raise TypeError('you must input the breed as a string')
    # pass the breed as the response.
    return _get(breed)

