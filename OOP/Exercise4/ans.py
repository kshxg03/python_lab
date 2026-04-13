class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            other_account.deposit(amount)
        else:
            print("Transfer failed. Check amount.")


account_1 = BankAccount("Kshitiz")
account_2 = BankAccount("Yosh")

account_1.deposit(1000)
account_2.deposit(500)

account_1.withdraw(200)
account_2.withdraw(100)

account_1.transfer(200, account_2)

print(f"{account_1.owner} Balance:", account_1.get_balance())
print(f"{account_2.owner} Balance:", account_2.get_balance())