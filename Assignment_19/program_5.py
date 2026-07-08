def GetPrime(no):
    facts = []
    for i in range(2, no+1):
        if no % i == 0:
            facts.append(i)

    if len(facts) == 1:
        return True
    else:
        return False

def MyFilter(data):
    filtered = []
    for i in data:
        if GetPrime(i) == True:
            filtered.append(i)
    return filtered

def MyMap(data):
    mapped = []
    for i in data:
        mapped.append(i * 2)

    return mapped

def MyReduce(data):
    max = 0
    for i in range(len(data)):
        if max < data[i]:
            max = data[i]

    return max

def main():
    data = []
    no = int(input("Enter the number: "))
    print(f"Enter {no} numbers: ")
    for i in range(no):
        data.append(int(input()))

    filteredData = MyFilter(data)
    print("After filter:", filteredData)
    mappedData = MyMap(filteredData)
    print("After Map:", mappedData)
    MaxNo = MyReduce(mappedData)
    print("Max number is: ", MaxNo)


if __name__ == "__main__":
    main()