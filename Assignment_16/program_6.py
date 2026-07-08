def CheckNo(no):
    if no > 0:
        return "Positive Number"
    elif no < 0:
        return "Negative Number"
    else:
        return "Zero"
    
def main():
    no = int(input("Enter the number:"))
    print(CheckNo(no))

if __name__ == "__main__":
    main()