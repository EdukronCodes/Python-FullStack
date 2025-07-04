# Base Class (Level 1)
class __________:
    def __init__(self, brand):
        self.brand = brand
        print(f"[Vehicle] Initialized for brand: {self.brand}")

    def __________(self):
        print(f"[Vehicle] Starting engine of {self.brand}")

# Derived Class (Level 2)
class __________(__________):
    def __init__(self, brand, model):
        __________.__init__(self, brand)  # Call base class constructor
        self.model = model
        print(f"[Car] Initialized for model: {self.model}")

    def __________(self):
        print(f"[Car] Driving {self.brand} {self.model}")

# Derived Class (Level 3)
class __________(__________):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range
        print(f"[ElectricCar] Initialized with range: {self.battery_range} km")

    def __________(self):
        print(f"[ElectricCar] Charging {self.brand} {self.model}... Range: {self.battery_range} km")

    def __________(self):  # Override base method
        print(f"[ElectricCar] No engine to start. {self.brand} {self.model} is electric!")

# Object creation and method calls
my_electric_car = __________("Tesla", "Model 3", 500)

my_electric_car.__________()
my_electric_car.__________()
my_electric_car.__________() 