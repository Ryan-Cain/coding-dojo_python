# Create a User class with an __init__ method
# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
# Add a display_user_balance method to the User class that displays user's account balance
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which 
# account they are withdrawing or depositing to
# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount
# and a different User instance, and transfers money from the user's account into another user's account.


# BankAccount Class
class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


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


# User Class

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
        self.accounts['account1'] = BankAccount(int_rate=0.2, balance=0)
        self.accounts['account2'] = BankAccount(int_rate=0.2, balance=0)

    def make_deposit(self, account, amount):
        self.accounts[account].deposit(amount)

    def make_withdrawal(self,account, amount):
        self.accounts[account].withdraw(amount)

    def display_user_balance(self, account):
        self.accounts[account].display_account_info()

    def transfer_money(self, amount, other_user, account):
        print(f'Transferring ${amount} from {self.name} to {other_user.name}')
        other_user.make_deposit(account, amount)
        self.make_withdrawal(account, amount)

user1 = User('Ryan', 'rcain@email.com')
user1.make_deposit('account1', 50)
user1.make_withdrawal('account1', 100)
user1.display_user_balance('account1')

user2 = User('Stephanie', 'scain@email.com')
user2.make_deposit('account1', 500)
user2.make_withdrawal('account1', 1000)
user2.display_user_balance('account1')

user2.transfer_money(250, user1, account='account1')
user2.display_user_balance('account1')
user1.display_user_balance('account1')

