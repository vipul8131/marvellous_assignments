# Write a lambda function using filter() which accepts list of strings and returns list of strings which is having length is greater than 5
MaxLenStr = lambda myStr: len(myStr) > 5

def main():
    strings = ["Hi", "Maharashtra", "Pune", "Python", "Mumbai", "data", "Anaconda", "India", "Nashik", "name", "phone"]
    print("List of strings:", list(filter(MaxLenStr, strings)))

if __name__ == "__main__":
    main()