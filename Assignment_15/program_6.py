# Write a lambda function using reduce() which accepts a list of numbers and return minimum number:
from functools import reduce
MinNo = lambda no1, no2: no1 if no1 < no2 else no2

def main():
    data = [23,1,44,23,65,77,33,249,78,90,111,99,224,34,89]
    print("The minimum number is:", reduce(MinNo, data))

if __name__ == "__main__":
    main()