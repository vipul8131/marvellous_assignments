# write a lambda function using reduce() which accepts list of number and returns a addition of all numbers:
from functools import reduce

AdditionList = lambda no1, no2: no1 + no2

def main():
    data = [23,45,10,78,34,8,3,17]
    print("Addition List is:", reduce(AdditionList, data))

if __name__ == "__main__":
    main()