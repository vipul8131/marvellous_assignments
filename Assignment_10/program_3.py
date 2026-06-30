# Write a program which accepts one number and prints factorial of that number.
def Fact(no):
    facts = 1
    for i in range(1, no+1):
        facts *= i

    return facts

def main():
    no = int(input("enter the number: "))
    print("Factorial of", no, "is: ", Fact(no))

if __name__ == "__main__":
    main()