#!/usr/bin/python3
"""
This script defines a function called validUTF8
"""


def validUTF8(data):
    """
    This finction checks if a given sequence of
    integers represents valid UTF-8 encoded data
    """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
