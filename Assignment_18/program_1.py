from functools import reduce
def Addtion(no1, no2):
    return no1 + no2

def main():
    data = []
    no = int(input("Enter the number: "))
    print(f"Enter {no} numbers: ")
    for i in range(no):
        f = int(input())
        data.append(f)

    print("Addition of list of data: ", reduce(Addtion, data))

if __name__ == "__main__":
    main()