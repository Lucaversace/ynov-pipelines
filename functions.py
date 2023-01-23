import json


def addition(a, b):
    """
    This function return the sum of a and b
    >>> addition(2,3)
    '5'
    """
    val = int(a) + int(b)
    return json.dumps(val)
