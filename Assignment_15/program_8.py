# Write a lambda function using filter() which accepts list of number and returns a list of number which is divisible by 3 and 5
DivBy3And5 = lambda no: no % 3 == 0 and no % 5 == 0

def main():
    data = [15,5,3,30,18,45,89,90]
    print("Numbers are divisible by 3 and 5 are:", list(filter(DivBy3And5, data)))

if __name__ == "__main__":
    main()