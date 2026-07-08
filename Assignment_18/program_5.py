from MarvellousNum import ChkPrime
from functools import reduce
def ListPrime(data):
    primList = list(filter(ChkPrime, data))
    print("Prime List: ", primList)
    sum = reduce(AddPrime, primList)
    return sum

def AddPrime(no1, no2):
    return no1 + no2

def main():
    myList = []
    no = int(input("Enter the number: "))
    print(f"Enter the {no} numbers:")
    for i in range(no):
        myList.append(int(input()))
    
    print(f"Addition of all prime numbers {ListPrime(myList)}")   

if __name__ == "__main__":
    main()