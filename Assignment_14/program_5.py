# Write a lambda function which accept one number and returns True if number is Even otherwise return False.
IsEven = lambda no: True if no % 2 == 0 else False

def main():
    no = int(input("Enter the number: "))
    print(no, "is even?:", IsEven(no))

if __name__ == "__main__":
    main()