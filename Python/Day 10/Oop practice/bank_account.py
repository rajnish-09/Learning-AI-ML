# Create BankAccount class with acc_number, name, balance and methods to deposit, withdraw and checkbalance

class BankAccount:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name  = name
        self.balance = balance

    def deposit(self, amount):
        if amount<0:
            print("Invalid amount.")
        else:
            self.balance += amount
        print(f"New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <0:
            print("Invalid amount")
        else:
            self.balance -= amount
        print(f'Remaining balance: {self.balance}')

    def check_balance(self):
        print(f'Current balance: {self.balance}')

        
b1 = BankAccount("101", "Rajnish", 10_000)
b1.deposit(5_000)
b1.withdraw(2_000)
b1.check_balance()