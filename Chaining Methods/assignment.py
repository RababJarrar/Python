
class User:
    def __init__(self,name):
        self.name=name
        self.account_balance=0

    def make_deposit(self,amount):     #method
        self.account_balance+= amount

    def make_withdrawl(self,amount):     #method
        self.account_balance-= amount
    def display_user_balance(self):
        print("User:",self.name,"balance:",self.account_balance)

rabab=User("RABAB")
hadeel=User("HADEEL")
maryam=User("MARYAM")

rabab.make_deposit(100)
rabab.make_deposit(200)
rabab.make_deposit(300)
rabab.make_withdrawl(400)
rabab.display_user_balance()

hadeel.make_deposit(1000)
hadeel.make_deposit(500)
hadeel.make_withdrawl(500)
hadeel.make_withdrawl(500)
hadeel.display_user_balance()

maryam.make_deposit(1000)
maryam.make_withdrawl(200)
maryam.make_withdrawl(200)
maryam.make_withdrawl(200)
maryam.display_user_balance()