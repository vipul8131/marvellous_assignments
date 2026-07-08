from functools import reduce

def ProductsNo(data):
    filteredData = list(filter(lambda no: (True if no >= 70 and no <= 90 else False), data))
    print("List after filter: ", filteredData)
    MappedData = list(map(lambda no: no + 10, filteredData))
    print("List after map: ", MappedData)
    return reduce(lambda no1, no2: no1 * no2, MappedData)

def main():
    data = []
    no = int(input("Enter the number: "))
    print(f"Enter the {no} numbers:")
    for i in range(no):
        data.append(int(input()))

    print(f"Product of number which is less than 90 and greater than 70 is: {ProductsNo(data)}")
    

if __name__ == "__main__":
    main()