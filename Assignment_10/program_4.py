# Write a program which accepts one number and print all even numbers till the number.
def getEvenNo(no):
    evenNo = []
    for i in range(1, no+1):
        if i % 2 == 0:
            evenNo.append(i)

    return evenNo

def main():
    no = int(input("Enter the number: "))
    print("even numbers of", no, "is: ", getEvenNo(no))

if __name__ == "__main__":
    main()