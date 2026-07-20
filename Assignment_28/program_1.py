import os
import sys

def main():
    args = sys.argv
    try:
        fobj = open(args[1], "r")
        print(f"Total number of lines in {args[1]} are {len(fobj.readlines())}")
        fobj.close()
    except:
        print(f"{args[1]} file is not exists in current directory.")


if __name__ == "__main__":
    main()