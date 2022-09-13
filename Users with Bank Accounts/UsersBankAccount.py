
class BankAccount:
    def __init__(self, int_rate=.02, balance=0):            #default value .02 , 0
        self.int_rate=int_rate                         
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance-=amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=amount
            return self

    def yield_interest(self):
        if(self.balance>0):
            self.balance=(1+self.int_rate)*self.balance
            return self
    
    def display_account_info(self):
        print("Balance: $",self.balance)




class User:
    def __init__(self,name):
        self.name=name
        self.account_balance=BankAccount( int_rate=.02, balance=0)

    def make_deposit(self,amount):     #method
        self.account_balance.deposit(amount)

    def make_withdrawl(self,amount):     #method
        self.account_balance.withdrawl(amount)
    
    def display_user_balance(self):
        self.account_balance.display_account_info()