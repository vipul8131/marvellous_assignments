# Write a program which accepts a number and print a multiplication table of that number
def MultiplicationTable(no):
    tables = []
    for i in range(1, 11):
        tables.append(no*i)

    return tables


def main():
    no = int(input("Enter the number for Multiplication Table: "))

    print(MultiplicationTable(no))

if __name__ == "__main__":
    main()