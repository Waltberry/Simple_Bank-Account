
"""
Created on Sun Nov 2021

@author: Walt
"""
class BankAccount(object):
    ''' Simple Bank Account simulator, it displays current amount
        can make deposit and also withdrawals.
    '''
    
    def __init__(self,balance=0.0):
        self.balance = balance
        
    def display_balance(self):
        print(f'Your balance is ${self.balance}')
        
    def make_deposit(self):
        amount = float(input('How much would you like to deposit?:>> $ '))
        self.balance += amount
        print(f'Balance is now ${self.balance}.')
        
    def make_withdrawal(self):
        amount = float(input('How much would you like to withdraw?:>> $ '))
        if amount > self.balance:
            print(f'Insufficient funds, your balance is ${self.balance}')
        else:
            self.balance -= amount
            print(f'Withdrawal successful:\n New balance is now ${self.balance}.')
            
   

