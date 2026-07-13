class Bookstore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        Bookstore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No. Of Books: {Bookstore.NoOfBooks}")

obj1 = Bookstore("Linux System Programing", "Robert Love")
obj1.Display()
obj2 = Bookstore("C Programming", "Dennis Ritchie")
obj2.Display()
obj3 = Bookstore("Chhava", "Shivaji Sawant")
obj3.Display()