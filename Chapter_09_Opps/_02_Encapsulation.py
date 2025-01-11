'''
Wrapping data and functions into a single unit (object)
'''
# Example 

class Account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.accountNo = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount , "was debited")
        print("total balance is ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount , "was credited")
        print("total balance is ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 95201041)
acc1.debit(1100)
acc1.credit(500)


   
