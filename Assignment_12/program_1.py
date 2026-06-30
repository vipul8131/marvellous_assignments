# Write a program which accept one character and checks whether it is vowel or consonent
def CheckChar(chr):
    vowel = ['A', 'E', 'I', 'O', 'U']
    if chr.upper() in vowel:
        return True
    else:
        return False
    
def main():
    st = input("Enter the character: ")
    if CheckChar(st) == True:
        print(st, "is Vowel")
    else:
        print(st, "is not Vowel")


if __name__ == "__main__":
    main()