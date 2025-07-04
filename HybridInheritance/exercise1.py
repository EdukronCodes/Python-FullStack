# Base Class
class __________:
    def __init__(self, name):
        self.name = name
        print(f"[Person] Initialized: {self.name}")

# Parent Class 1
class __________:
    def __________(self):
        print("[Employee] Working...")

# Parent Class 2
class __________:
    def __________(self):
        print("[Student] Studying...")

# Derived Class (Hybrid)
class __________(__________, __________, __________):
    def __init__(self, name):
        __________.__init__(self, name)
        print("[Intern] Initialized!")

    def __________(self):
        print(f"[Intern] {self.name} is interning!")

# Object creation and method calls
intern = __________("Alice")
intern.__________()
intern.__________()
intern.__________() 