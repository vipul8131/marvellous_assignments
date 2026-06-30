# Write a program which accepts one number and prints that many numbers starting from 1
def main():
    no = int(input("Enter the number: "))
    numbers = []
    for i in range(1, no+1):
        numbers.append(i)
    
    print("Numbers starting from 1: ", numbers)

if __name__ == "__main__":
    main()