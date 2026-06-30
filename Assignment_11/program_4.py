# Write a program which accepts a number and print reverse of that number:
def ReverseNo(no): # using str[::-1]
    return no[::-1]

def ReverseNo2(no): # Revese using loop
    reverse = ""
    length = len(no)
    for i in range(len(no)):
        reverse += no[length-1]
        length -= 1
    
    return reverse

def main():
    no = int(input("Enter the number: "))
    print("Reverse number of", no, "is: ", ReverseNo(str(no))) # Reverse using built in method
    print("Reverse2 number of", no, "is: ", ReverseNo2(str(no))) # Revese using loop
    

if __name__ == "__main__":
    main()