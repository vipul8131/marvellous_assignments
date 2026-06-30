# write a program which accepts a number and prints sum of digit
def SumOfDigit(no):
    sum =0
    for i in no:
        sum += int(i)

    return sum

def main():
    no = int(input("enter the number: "))
    print("Sum of", no, "is: ", SumOfDigit(str(no)))


if __name__ == "__main__":
    main()