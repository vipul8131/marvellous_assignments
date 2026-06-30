# Write a program which accepts a number and print sum of first N natural numbers
def SumOfNo(no):
    sum = 0
    for i in range(1, no+1):
        sum += i

    return sum

def main():
    no = int(input("Enter the number: "))
    print("Sum of Number of", no, "is: ", SumOfNo(no))

if __name__ == "__main__":
    main()