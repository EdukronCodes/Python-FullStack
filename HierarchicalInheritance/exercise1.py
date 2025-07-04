# Base Class
class __________:
    def __init__(self, name):
        self.name = name
        print(f"[Shape] Initialized: {self.name}")

    def __________(self):
        print(f"[Shape] Drawing {self.name}")

# Derived Class 1
class __________(__________):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f"[Circle] Radius: {self.radius}")

    def __________(self):
        print(f"[Circle] Area: {3.14 * self.radius * self.radius}")

# Derived Class 2
class __________(__________):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
        print(f"[Square] Side: {self.side}")

    def __________(self):
        print(f"[Square] Area: {self.side * self.side}")

# Object creation and method calls
c = __________("Circle", 5)
s = __________("Square", 4)
c.__________()
c.__________()
s.__________()
s.__________() 