class Arithmatic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter 1st number: "))
        self.value2 = int(input("Enter 2nd number: "))

    def Addition(self):
        return self.value1 + self.value2

    def Substraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1 / self.value2
    
obj1 = Arithmatic()
for i in range(2):
    obj1.Accept()
    ret = obj1.Addition()
    print("Addition: ", ret)
    ret = obj1.Substraction()
    print("Substraction: ", ret)
    ret = obj1.Multiplication()
    print("Multiplication: ", ret)
    ret = obj1.Division()
    print("Division: ", ret)
    print("="*50)



    
        