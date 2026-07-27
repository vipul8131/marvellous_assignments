import hashlib
import os
def CheckSum(filePath):
    fobj = open(filePath, "rb")
    hobj = hashlib.md5()
    buffer = fobj.read(1000)
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()