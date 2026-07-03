# Write a lambda function which accepts two numbers and returns maximum number.
MaxNo = lambda no1, no2: no1 if no1 > no2 else no2

def main():
    no1 = int(input("Enter 1st number: "))
    no2 = int(input("Enter 2nd number: "))
    print("Maximum number between", no1, "and", no2, "is: ", MaxNo(no1, no2))

if __name__ == "__main__":
    main()
