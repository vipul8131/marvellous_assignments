#Write a program which contains one function ChkGreater() that accepts two numbers and prints  the greater number.
def ChkGreater(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2
    
def main():
    no1 = int(input("Enter 1st number: "))
    no2 = int(input("Enter 2nd number: "))

    print(ChkGreater(no1, no2), "is greater")


if __name__ == "__main__":
    main()