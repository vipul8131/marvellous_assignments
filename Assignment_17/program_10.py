def Add(no):
    sum = 0
    for i in str(no):
        sum += int(i)

    return sum

def main():
    no = int(input("Enter the number: "))
    print(f"Addition of {no} is: {Add(no)}")
     
if __name__ == "__main__":
    main()