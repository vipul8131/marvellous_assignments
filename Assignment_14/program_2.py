# Write a lambda function which accept one number and returns a cube of number.
Cube = lambda no: no ** 3
def main():
    no = int(input("Enter the number: "))
    print("Cube of", no, "is: ", Cube(no))

if __name__ == "__main__":
    main()