def ChkNum(no):
    return True if no % 2 == 0 else False

def main():
    no = int(input("Enter the number: "))
    if ChkNum(no) == True:
        print("Even Number.")
    else:
        print("Odd Number.")

if __name__ == "__main__":
    main()