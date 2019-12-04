from .utils import _get

# DISCLAMER: This code was taken from https://github.com/joebeachjoebeach/dog-api. All credit
# for this section of the code belongs to the original author "joebeachjoebeach". 

def master_breeds():
    """Gets all breeds, not including sub-breeds. Returns a list of breed names."""
    return _get('breeds/list')


def subbreeds(breed):
    """Gets the list of sub-breeds from the chosen breed. Returns a list of sub-breeds."""
    if not isinstance(breed,str):
        raise TypeError('you must input the breed as a string')
    return _get('breed/{0}/list'.format(breed))

def random_image(breed=None, subbreed=None):
    """Gets a random dog image. Returns a url as a string"""
    if breed == None and subbreed == None:
        return _get('breeds/image/random')
    elif subbreed == None:
        return _get('breed/{0}/images/random'.format(breed))
    else:
        return _get('breed{0}/{1}/images/random'.format(breed,subbreed))
