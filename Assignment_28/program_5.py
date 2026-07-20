import sys

def main():
    args = sys.argv
    try:
        fobj = open(args[1], "r")

        if fobj.read().lower().count(args[2].lower()):
            print(f"{args[2]} is found in {args[1]}")
        else:
            print(f"{args[2]} is not found in {args[1]}")

        fobj.close()
        
    except:
        print("file not found.")

if __name__ == "__main__":
    main()