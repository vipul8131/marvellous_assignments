# Write a program which accepts one number and check whether number is prime or not.
def CheckPrimeOrNot(no):
    facto = 0
    for i in range(1, no+1):
        if no % i == 0:
            facto += 1
    
    if facto > 2:
        return False
    else:
        return True
        
def main():
    no = int(input("Enter the number: "))
    if(CheckPrimeOrNot(no) == True):
        print(no, "is a prime number")
    else:
        print(no, "is not a prime number")

if __name__ == "__main__":
    main()