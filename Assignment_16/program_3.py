def Add(no1, no2):
    return no1 + no2

def main():
    no1 = int(input("Enter 1st number:"))
    no2 = int(input("Enter 2nd number:"))
    print(f"Addition: {Add(no1, no2)}")

if __name__ == "__main__":
    main()