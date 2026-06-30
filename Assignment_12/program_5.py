# Write a program which accepts one number and prints that many numbers in reverse order
def main():
    no = int(input("Enter the number: "))
    numbers = []
    for i in range(no, 0, -1):
        numbers.append(i)
    
    print("Numbers in reverse order: ", numbers)

if __name__ == "__main__":
    main()