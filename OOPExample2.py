class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance = {self.balance}")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                print("Withdrawal amount must be positive")
                return
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance for this withdrawal")
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance = {self.balance}")
        except InsufficientBalanceError as e:
            print(f"Error: {e}")

    def display_balance(self):
        print(f"Account {self.account_number} ({self.holder_name}) balance = {self.balance}")

    def display_transactions(self):
        print(f"\nTransaction history for {self.holder_name}:")
        if not self.transaction_history:
            print("No transactions yet")
        for transaction in self.transaction_history:
            print(f"- {transaction}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=4.0):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        self.transaction_history.append(f"Interest added: {interest:.2f}")
        print(f"Interest of {interest:.2f} added. New balance = {self.balance:.2f}")


def main():
    acc_number = input("Enter account number: ")
    holder_name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))
    rate = float(input("Enter interest rate (%): "))

    account = SavingsAccount(acc_number, holder_name, initial_balance, rate)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Add Interest\n4. Display Balance\n5. Display Transactions\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "3":
            account.add_interest()
        elif choice == "4":
            account.display_balance()
        elif choice == "5":
            account.display_transactions()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()