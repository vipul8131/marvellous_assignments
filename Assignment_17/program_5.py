def CheckPrime(no):
    facts = []
    for i in range(2, no+1):
        if no % i == 0:
            facts.append(i)
    
    if(len(facts) == 1):
        return True
    else:
        return False

def main():
    no = int(input("Enter the number: "))
    if CheckPrime(no) == True:
        print(f"{no} is Prime Number.")
    else:
        print(f"{no} is not a Prime Number.")
    
     
if __name__ == "__main__":
    main()