from functools import reduce

def SquareNo(data):
    filteredData = list(filter(lambda no: (True if no % 2 == 0 else False), data))
    print("List after filter: ", filteredData)
    MappedData = list(map(lambda no: no ** 2, filteredData))
    print("List after map: ", MappedData)
    return reduce(lambda no1, no2: no1 + no2, MappedData)

def main():
    data = []
    no = int(input("Enter the number: "))
    print(f"Enter the {no} numbers:")
    for i in range(no):
        data.append(int(input()))

    print(f"Output of Reduce: {SquareNo(data)}")
    

if __name__ == "__main__":
    main()