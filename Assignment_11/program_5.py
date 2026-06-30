# Write a program which accepts a number and check whether it is palindrome or not
def CheckPalindrome(no):
    no = str(no)
    reverseNo = no[::-1]
    if no == reverseNo:
        return True
    else:
        return False
    
def main():
    no = int(input("Enter the number: "))
    if CheckPalindrome(no) == True:
        print("Number is palindrome.")
    else:
        print("Number is not Palindrome.")

if __name__ == "__main__":
    main()