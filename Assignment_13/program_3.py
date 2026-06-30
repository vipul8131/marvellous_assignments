# Write a program which accepts one number and check whether it is perfect number or not.
def CheckPerfectNo(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum += i

    if sum == no:
        return True
    else:
        return False
    
def main():
    no = int(input("Enter the number: "))
    if CheckPerfectNo(no) == True:
        print(no, "is perfect number.")
    else:
        print(no,"is not perfect number.")

if __name__ == "__main__":
    main()