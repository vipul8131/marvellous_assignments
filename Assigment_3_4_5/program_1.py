# Write a program to Display bellow:
# -Data Type
# -Memory Address
# -Size in bytes of variable entered by the User

import sys

def main():
    data = input("Enter the value:")

    # show datatype
    print("Datatype of ", data, " is: ", type(data))

    # Memory Address
    print("Memory Address: ", id(data))

    # Size in bytes
    print("Size of ", data, " is: ", sys.getsizeof(data))

if __name__ == "__main__":
    main()
