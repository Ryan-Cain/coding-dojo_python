# Create a BankAccount class with the attributes interest rate and balance
# Add a deposit method to the BankAccount class
# Add a withdraw method to the BankAccount class
# Add a display_account_info method to the BankAccount class
# Add a yield_interest method to the BankAccount class
# Create 2 accounts
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def show_all_accounts(cls):
        accountNum = 1
        for account in cls.all_accounts:
            print(f'Account {accountNum} balance is {account.balance}, and interest rate is {account.int_rate}')
            accountNum += 1

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited ${amount}, account balance is now ${self.balance}')
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'Withdrew ${amount}, account balance is now ${self.balance}')
        else:
            self.balance -= 5
            print(f"Insufficient funds: Tried to withdraw ${amount}, charging a $5 fee, account balance is now ${self.balance}")
        return self
    
    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > -1:
            self.balance += self.balance * self.int_rate
            print(f'Applied interest rate of {int(self.int_rate*100)}%')
        return self
    

account1 = BankAccount(.01).deposit(20).deposit(100).deposit(475).withdraw(500).yield_interest().display_account_info()
account2 = BankAccount(.04).deposit(100).deposit(125).withdraw(50).withdraw(75).withdraw(50).withdraw(75).yield_interest().display_account_info()
account3 = BankAccount(.06).deposit(100).deposit(200).withdraw(50).withdraw(25).withdraw(50).withdraw(75).yield_interest().display_account_info()

BankAccount.show_all_accounts()
