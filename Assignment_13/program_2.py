# Write a program which accepts radius of circle and print area of circle.
def Area(radius):
    return 3.14 * (radius * radius)

def main():
    radius = float(input("Enter the radius of Circle: "))

    print("Area of Circle is:", Area(radius))

if __name__ == "__main__":
    main()
