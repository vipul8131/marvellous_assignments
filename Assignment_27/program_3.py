class Numbers:
    factorList = []
    def __init__(self, value):
        self.value = value

    def ChkPrime(self):
        facts = []
        for i in range(2, self.value+1):
            if no % i == 0:
                facts.append(i)

        if len(facts) == 1:
            return True
        else:
            return False


    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.value):
            if no % i == 0:
                sum += i

        if sum == self.value:
            return True
        else:
            return False

    def Factors(self):
        Numbers.factorList = []
        for i in range(1, self.value):
            if no % i == 0:
                Numbers.factorList.append(i)
        
        print(f"Factors of {self.value} are: {Numbers.factorList}")

        

    def SumFactors(self):
        sum = 0
        for i in Numbers.factorList:
            sum += i

        return sum
    
no = int(input("Enter the number: "))
obj = Numbers(no)

print(f"This {"is" if obj.ChkPrime() == True else "is not a"} prime number")
print(f"This {"is" if obj.ChkPerfect() == True else "is not a"} perfect number")
obj.Factors()
print(f"Sum pf factors of {no} is :", obj.SumFactors())

