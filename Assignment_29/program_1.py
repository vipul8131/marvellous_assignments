import sys
import os

def main():
    args = sys.argv
    if os.path.exists(args[1]):
        print(f"{args[1]} file is exists in current directory.")
    else:
        print(f"{args[1]} file is not exists in current directory.")

if __name__ == "__main__":
    main()