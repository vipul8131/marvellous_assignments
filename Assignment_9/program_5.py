# Write a program which accept one number and print cube of it
def CheckDevisible(no):
    if(no % 3 == 0 and no % 5 == 0):
        return True
    else:
        return False
    
def main():
    no = int(input("Enter the number: "))
    if CheckDevisible(no):
        print("Devisible by 3 and 5")
    else:
        print("Not Devisible by 3 and 5")

if __name__ == "__main__":
    main()