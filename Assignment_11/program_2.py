# Write a program which accepts a number and print count of digit in that number.
def main():
    no = int(input("Enter the number: "))
    no = str(no)
    print("The digit count in", no, "is: ", len(no))


if __name__ == "__main__":
    main()
