# Base Class
class Employee:
    def __init__(self, name):
        self.name = name
        print(f"[Employee] Name: {self.name}")

    def work(self):
        print(f"[Employee] Working: {self.name}")

# Derived Class 1
class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
        print(f"[Manager] Department: {self.department}")

    def manage(self):
        print(f"[Manager] Managing {self.department}")

# Derived Class 2
class Developer(Employee):
    def __init__(self, name, project):
        super().__init__(name)
        self.project = project
        print(f"[Developer] Project: {self.project}")

    def code(self):
        print(f"[Developer] Coding for {self.project}")

# Object creation and method calls
mgr = Manager("Alice", "HR")
dev = Developer("Bob", "AI")
mgr.manage()
mgr.work()
dev.code()
dev.work() 