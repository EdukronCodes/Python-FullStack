# Base Class
class __________:
    def __init__(self, name):
        self.name = name
        print(f"[Animal] Initialized: {self.name}")

    def __________(self):
        print(f"[Animal] {self.name} is making a sound.")

# Derived Class
class __________(Animal):
    def __init__(self, name, breed):
        __________.__init__(self, name)
        self.breed = breed
        print(f"[Dog] Initialized: {self.breed}")

    def __________(self):
        print(f"[Dog] {self.name} the {self.breed} is barking!")

# Object creation and method calls
my_dog = __________("Buddy", "Labrador")

my_dog.make_sound()
my_dog.__________() 