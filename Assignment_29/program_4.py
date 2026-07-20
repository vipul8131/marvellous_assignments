import sys
import os
import hashlib

def CalculateCheckSum(file):
    fobj = open(file, "rb")
    hobj = hashlib.md5()
    buffer = fobj.read(1000)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1000)

    return hobj.hexdigest()

def main():
    args = sys.argv
    
    checkSum1 = CalculateCheckSum(args[1])
    checkSum2 = CalculateCheckSum(args[2])

    if checkSum1 == checkSum2:
        print("Success! Both files are same.")
    else:
        print("Failed! Both files are not same.")


if __name__ == "__main__":
    main()