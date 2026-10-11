class Account:
    def __init__(self,balance):
        self.balance=balance
        pass

    def get_balance(self):
        print("Current balance:",self.balance)

    def credit(self,amount):
        self.balance=self.balance + amount
        print("Updated balance:",self.balance)

    def debit(self,amount):
        self.balance=self.balance -amount
        print("Updated balance:",self.balance)

s1=Account(5000)
s1.get_balance()
s1.credit(2000)
s1.debit(500)
s1.get_balance()
