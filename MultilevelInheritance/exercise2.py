# Base Class
class Device:
    def __init__(self, name):
        self.name = name
        print(f"[Device] Name: {self.name}")

    def power_on(self):
        print(f"[Device] Powering on {self.name}")

# Derived Class 1
class Computer(Device):
    def __init__(self, name, os):
        super().__init__(name)
        self.os = os
        print(f"[Computer] OS: {self.os}")

    def boot(self):
        print(f"[Computer] Booting {self.name} with {self.os}")

# Derived Class 2
class Laptop(Computer):
    def __init__(self, name, os, version):
        super().__init__(name, os)
        self.version = version
        print(f"[Laptop] Version: {self.version}")

    def run(self):
        print(f"[Laptop] {self.name} running {self.os} v{self.version}")

# Object creation and method calls
my_laptop = Laptop("ThinkPad", "Windows", "10")
my_laptop.power_on()
my_laptop.boot()
my_laptop.run() 