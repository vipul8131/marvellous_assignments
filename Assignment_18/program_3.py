from functools import reduce
def Min(no1, no2):
    return no1 if no1 < no2 else no2

def main():
    myList = []
    no = int(input("Enter the number: "))
    print(f"Enter the {no} numbers:")
    for i in range(no):
        myList.append(int(input()))

    print(f"Minimum number from the list is {reduce(Min, myList)}")   

if __name__ == "__main__":
    main()