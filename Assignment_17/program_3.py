def Facto(no):
    facts = 1
    for i in range(1, no+1):
        facts *= i

    return facts

def main():
    no = int(input("Enter the number: "))
    print(f"Factorial of {no} is: {Facto(no)}")
    
     
if __name__ == "__main__":
    main()