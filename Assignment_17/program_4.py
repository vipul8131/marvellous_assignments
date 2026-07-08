def SumFact(no):
    facts = []
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            facts.append(i)
            sum += i
    print(facts)
    return sum

def main():
    no = int(input("Enter the number: "))
    print(f"Sum of {no} factorials is: {SumFact(no)}")
    
     
if __name__ == "__main__":
    main()