# Base Class
class __________:
    def __init__(self, name):
        self.name = name
        print(f"[Device] Name: {self.name}")

# Parent Class 1
class __________:
    def __________(self):
        print("[Camera] Taking photo...")

# Parent Class 2
class __________:
    def __________(self):
        print("[Phone] Making call...")

# Derived Class (Hybrid)
class __________(__________, __________, __________):
    def __init__(self, name):
        __________.__init__(self, name)
        print("[Smartphone] Ready!")

    def __________(self):
        print(f"[Smartphone] {self.name} is smart!")

# Object creation and method calls
sp = __________("Pixel")
sp.__________()
sp.__________()
sp.__________() 