import sys
import os
def getQName_from_URI(uriName):
    indexChar = uriName.index("#")
    return uriName[indexChar+1:]
def is_Float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def is_Int(str):
    try:
        int(float(str))
        return True
    except ValueError:
        return False