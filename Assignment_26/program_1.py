class Demo:
    Value = 10

    def __init__(self, no1, no2):
        self.a = no1
        self.b = no2

    def Fun(self):
        print(f"no1: {self.a}")
        print(f"no2: {self.b}")

    def Gun(self):
        print(f"no1: {self.a}")
        print(f"no2: {self.b}")

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()