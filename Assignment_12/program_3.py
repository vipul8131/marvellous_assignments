# Write a program which accepts 2 number and print Addition, Substraction, Multiplication and Division.
def Calculations(no1, no2):
    adds = no1 + no2
    sub = no1 - no2
    mul = no1 * no2
    div = no1 / no2

    return adds, sub, mul, div

def main():
    no1 = int(input("Enter 1st number: "))
    no2 = int(input("Enter 2nd number: "))

    adds, sub, mul, div = Calculations(no1, no2)
    print("Addition: ", adds)
    print("Substraction: ", sub)
    print("Divsion: ", div)
    print("Multiplication: ", mul)


if __name__ == "__main__":
    main()