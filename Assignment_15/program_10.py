# Write a lambda function using filter() which accepts list of numbers and return of count of even number
CountEvnNo = lambda no: no % 2 == 0
def main():
    data = [12,34,67,33,90,75,45,88,62,55]
    print("Count of even numbers:", len(list(filter(CountEvnNo, data))))

if __name__ == "__main__":
    main()