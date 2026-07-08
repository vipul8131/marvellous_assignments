def SearchNo(no, data):
    return data.count(no)

def main():
    myList = []
    no = int(input("Enter the number: "))
    print(f"Enter the {no} numbers:")
    for i in range(no):
        myList.append(int(input()))
    
    f = int(input("Enter search number: "))


    print(f"Frequency of {f} is: {SearchNo(f, myList)}")   

if __name__ == "__main__":
    main()