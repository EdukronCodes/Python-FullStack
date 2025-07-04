# Base Class
class __________:
    def __init__(self, name):
        self.name = name
        print(f"[Vehicle] Name: {self.name}")

    def __________(self):
        print(f"[Vehicle] Moving: {self.name}")

# Derived Class 1
class __________(__________):
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels
        print(f"[Bike] Wheels: {self.wheels}")

    def __________(self):
        print(f"[Bike] Riding with {self.wheels} wheels")

# Derived Class 2
class __________(__________):
    def __init__(self, name, seats):
        super().__init__(name)
        self.seats = seats
        print(f"[Bus] Seats: {self.seats}")

    def __________(self):
        print(f"[Bus] Carrying {self.seats} passengers")

# Object creation and method calls
bike = __________("MountainBike", 2)
bus = __________("CityBus", 40)
bike.__________()
bike.__________()
bus.__________()
bus.__________() 