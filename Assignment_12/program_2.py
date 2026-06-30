# Write a program which accepts a number and prints its factor
def getFactors(no):
    factors = []
    for i in range(1, no+1):
        if no % i == 0:
            factors.append(i)
    
    return factors

def main():
    no = int(input("Enter the number: "))
    print("Factors of", no, "is: ", getFactors(no))


if __name__ == "__main__":
    main()