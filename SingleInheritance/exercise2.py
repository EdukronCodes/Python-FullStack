# Base Class
class Fruit:
    def __init__(self, color):
        self.color = color
        print(f"[Fruit] Color: {self.color}")

    def describe(self):
        print(f"[Fruit] This fruit is {self.color}.")

# Derived Class
class Apple(Fruit):
    def __init__(self, color, taste):
        super().__init__(color)
        self.taste = taste
        print(f"[Apple] Taste: {self.taste}")

    def describe(self):
        print(f"[Apple] This apple tastes {self.taste}.")

# Object creation and method calls
my_apple = Apple("Red", "Sweet")
my_apple.describe()
my_apple.describe() 