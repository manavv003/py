class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        # Private attributes
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance for this withdrawal.")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")

    def get_balance(self):
        """Return the current balance."""
        return self.__balance


# Example usage:
account = BankAccount("123456789", 1000)  # Create an account with a balance of $1000

# Deposit money
account.deposit(500)  # Deposit $500

# Withdraw money
account.withdraw(200)  # Withdraw $200

# Get balance
print(f"Current Balance: ${account.get_balance()}")  # Print updated balance
