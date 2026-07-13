class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account holder name: ", self.Name)
        print("Account Balance: ", self.Amount)

    def Deposit(self, value):
        self.Amount += value

    def Withdraw(self, value):
        if self.Amount != 0 and self.Amount > value:
            self.Amount -= value
        else:
            print("======Insuficient balance.=======")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    

obj1 = BankAccount("Peter parker", 1000)
obj1.Display()
print("Interest: ", obj1.CalculateInterest())
obj1.Deposit(int(input("Enter the amount for deposit: ")))
obj1.Display()
print("Interest: ", obj1.CalculateInterest())
obj1.Withdraw(int(input("Enter the amount for withdraw:")))
obj1.Display()
print("Interest: ", obj1.CalculateInterest())

