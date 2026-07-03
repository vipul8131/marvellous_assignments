# Write a lambda function using filter() which accepts a list of number and returns a list of Odd number.
OddNoList = lambda no: no % 2 != 0

def main():
    data = [23,44,62,9,10,34,77,66,78,13,99]
    print("Even number list:", list(filter(OddNoList, data)))

if __name__ == "__main__":
    main()