import sys

def main():
    args = sys.argv
    fobj1 = open(args[1], "w+")
    fobj2 = open(args[2], "r")

    data = fobj2.readlines().copy()

    for fdata in data:
        fobj1.write(fdata)

    print("File copied succesfully.")

    fobj1.close()
    fobj2.close()
    

if __name__ == "__main__":
    main()