
class User:
    def __init__(self,name):
        self.name=name
        self.account_balance=0

    def make_deposit(self,amount):     #method
        self.account_balance+= amount
        return self
    def make_withdrawl(self,amount):     #method
        self.account_balance-= amount
        return self
    def display_user_balance(self):
        print("User:",self.name,"balance:",self.account_balance)
       
rabab=User("RABAB")
hadeel=User("HADEEL")
maryam=User("MARYAM")

rabab.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawl(400).display_user_balance()

hadeel.make_deposit(1000).make_deposit(500).make_withdrawl(500).make_withdrawl(500).display_user_balance()

maryam.make_deposit(1000).make_withdrawl(200).make_withdrawl(200).make_withdrawl(200).display_user_balance()