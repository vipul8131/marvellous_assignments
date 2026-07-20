import sys

def main():
    args = sys.argv
    fobj = open(args[1], "r")
    word_count = len(fobj.read().split())
    print(f"Total number of words in {args[1]} are: {word_count}")

if __name__ == "__main__":
    main()