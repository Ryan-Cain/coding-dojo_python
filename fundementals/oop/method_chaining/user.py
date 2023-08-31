# On instantiation of a user, the following attributes should be passed in as arguments:
# Attributes
# first_name, last_name, email, age
# Also include default attributes:
# is_rewards_member - default value of False
# gold_card_points = 0

# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.

# Ninja Bonuses:
# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.

class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member='False', gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    
    def display_info(self, called_from="class"):
        print(f'''
            Called From: {called_from}
            First Name: {self.first_name}
            Last Name: {self.last_name}
            Email: {self.email}
            Age: {self.age}
            Rewards Member: {self.is_rewards_member}
            Gold Card Points: {self.gold_card_points}
              ''')
        return self
        
    def enroll(self):
        if self.is_rewards_member:
            print(f'{self.first_name} is already a member')
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        self.display_info('enroll')
        return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f'Sorry {self.first_name}, you do not have the funds')
        else:
            print(f'{self.first_name} is spending {amount} points')
            self.gold_card_points -= amount
        self.display_info('spend_points')
        return self



user1 = User('Ryan', 'Cain', 'something@hotmail.com', 30, True, 1200)
user2 = User('Tony', 'Stark', 'avenge@hotmail.com', 42, False, 0)
user3 = User('Abe', 'Lincoln', 'pres@hotmail.com', 50, True, 1863)

user1.display_info().spend_points(50).enroll()
user2.enroll().spend_points(80)
user3.spend_points(2000)
