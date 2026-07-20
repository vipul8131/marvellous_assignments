import sys
import os

def main():
    searchStr = sys.argv[2]
    fobj = open(sys.argv[1], "r")
    data = fobj.read()

    searchCnt = data.count(searchStr)
    print(f"There are {searchCnt} occurence found in {sys.argv[1]}.")
    

if __name__ == "__main__":
    main()