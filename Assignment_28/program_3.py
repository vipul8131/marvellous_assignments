import sys

def main():
    args = sys.argv
    fobj = open(args[1], "r")
    data = fobj.read().split(".")
    for lines in data:
        print(lines)

    fobj.close()

if __name__ == "__main__":
    main()