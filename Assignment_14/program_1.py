# Write lambda function which accepts one number and returns square of that number.
Square = lambda no: no*no

def main():
    no = int(input("Enter the number: "))
    print("Square of", no, "is: ", Square(no))

if __name__ == "__main__":
    main()