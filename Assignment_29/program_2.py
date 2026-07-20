import sys

def main():
    args = sys.argv
    fobj = open(args[1], "r")

    print("File content: ", fobj.read())

    fobj.close()

if __name__ == "__main__":
    main()