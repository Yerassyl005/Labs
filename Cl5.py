""" Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed 
    the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't 
    be overdrawn.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds the available balance. Transaction denied.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from the balance")

    def display_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount("John Doe")

account.deposit(1000)
account.display_balance()

account.withdraw(500)
account.display_balance() 

account.withdraw(600) 
account.display_balance()