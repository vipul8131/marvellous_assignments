# Write a lambda function which accepts two numbers and return addition.
Addition = lambda no1, no2: no1 + no2
def main():
    no1 = int(input("Enter 1st number: "))
    no2 = int(input("Enter 2nd number: "))
    print("Addition: ", Addition(no1, no2))

if __name__ == "__main__":
    main()