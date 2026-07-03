# Write a lambda function using reduce() which accepts list of number and return product of all numbers.
from functools import reduce
products = lambda no1, no2: no1 * no2

def main():
    data = [20,34,11,44,22,56]
    print("Product of all numbers:", reduce(products, data))

if __name__ == "__main__":
    main()