class BankAccount:
    def __init__(self, initial_balance=0):
        # This is the setup. If no money is given, it starts at 0.
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Add money to the pile
        self.account_balance += amount

    def withdraw(self, amount):
        # Check if we have enough money first!
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True  # Success! We took money out.
        else:
            return False  # Fail! Not enough money.

    def display_balance(self):
        # Show the money formatted nicely (e.g., $50.00)
        print(f"Current Balance: ${self.account_balance:.2f}")
