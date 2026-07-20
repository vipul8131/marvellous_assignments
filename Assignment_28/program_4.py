import sys
import os

def main():
    args = sys.argv

    try:
        fobj1 = open(args[2], "w+")
        fobj2 = open(args[1], "r")

        data = fobj2.readlines().copy()
        for lines in data:
            fobj1.write(lines)
        # print(not fobj1.read().strip())

        if not fobj1.read().strip():
            print(f"File data is copied successfully from {args[1]} and {args[2]}.")
        else:
            print("FIle data is not copied.")
            

        fobj1.close()
        fobj2.close()
    
    except Exception as expt:
        print(f"{args[1]} and {args[2]} files are not found. {expt}")

if __name__ == "__main__":
    main()