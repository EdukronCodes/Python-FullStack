# Base Class
class Account:
    def __init__(self, id):
        self.id = id
        print(f"[Account] ID: {self.id}")

# Parent Class 1
class Buyer:
    def buy(self):
        print("[Buyer] Buying...")

# Parent Class 2
class Seller:
    def sell(self):
        print("[Seller] Selling...")

# Derived Class (Hybrid)
class MarketplaceUser(Account, Buyer, Seller):
    def __init__(self, id):
        Account.__init__(self, id)
        print("[MarketplaceUser] Initialized!")

    def is_active(self):
        print(f"[MarketplaceUser] User {self.id} is active!")

# Object creation and method calls
user = MarketplaceUser(101)
user.buy()
user.sell()
user.is_active() 