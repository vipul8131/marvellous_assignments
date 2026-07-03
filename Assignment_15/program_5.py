# Write a lambda function using reduce() which accepts a list of numbers and return maximum number:
from functools import reduce
MaxNo = lambda no1, no2: no1 if no1 > no2 else no2

def main():
    data = [23,1,44,23,65,77,33,249,78,90,111,99,224,34,89]
    print("The maximum number is:", reduce(MaxNo, data))

if __name__ == "__main__":
    main()