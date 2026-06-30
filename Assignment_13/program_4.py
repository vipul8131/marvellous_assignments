# Write a program which accepts one number and prints binary equivalent
#8 = 1000
#13 = 1101
def ConvertBinaryNo(num):
    if num == 0:
        return "0"
        
    binary_str = ""
    while num > 0:
        remainder = num % 2
        # print("remainder: ", remainder)
        binary_str = str(remainder) + binary_str
        # print("binary_str: ", binary_str)
        num = num // 2
    return binary_str

def main():
    no = int(input("Enter the number: "))
    print("Binary number of", no, "is: ", ConvertBinaryNo(no))

if __name__ == "__main__":
    main()