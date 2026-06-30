# Write a program which accepts one number and prints all Odd numbers till the number.
def getOddNo(no):
    oddNo = []
    for i in range(1, no+1):
        if i % 2 != 0:
            oddNo.append(i)

    return oddNo

def main():
    no = int(input("Enter the number: "))
    print("Odd numbers of", no, "is: ", getOddNo(no))

if __name__ == "__main__":
    main()