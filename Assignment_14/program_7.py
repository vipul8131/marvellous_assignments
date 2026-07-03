# Write a lambda function which accepts one number and returns True if number is divisible by 5.
IsDivByFive = lambda no: True if no % 5 == 0 else False

def main():
    no = int(input("Enter the number: "))
    print(no, "is divisible by 5?:", IsDivByFive(no))

if __name__ == "__main__":
    main()
