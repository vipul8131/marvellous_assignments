# Write a lambda function which accepts three numbers and returns largest number.
LargestNo = lambda no1, no2, no3: no1 if no1 > no2 and no2 > no3 else (no2 if no2 > no3 else no3)

def main():
    no1 = int(input("Enter 1st number: "))
    no2 = int(input("Enter 2nd number: "))
    no3 = int(input("Enter 3rd number: "))

    print("The largest number between", no1, no2, no3, "is: ", LargestNo(no1,no2,no3))

if __name__ == "__main__":
    main()