# Write a program which accepts Width and length of reactangle and print area.
def Area(width, length):
    return width * length
def main():
    width = float(input("Enter the width of Rectangle: "))
    length = float(input("Enter the length of Rectangle: "))

    print("Area of Rectangle is:", Area(width, length))

if __name__ == "__main__":
    main()
