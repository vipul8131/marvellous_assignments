# Write a lambda function using map() which accepts list of numbers and returns list of square of each number.
SquareList = lambda no: no*no

def main():
    data = [23,45,8,19,20,12]
    result = list(map(SquareList, data))
    print("The list of square of each number is:", result)

if __name__ == "__main__":
    main()