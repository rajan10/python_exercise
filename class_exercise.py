class BankAccount:
    def __init__(self,account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"you deposited {amount} and your total balance is {self.balance}")
        return self.balance
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance= self.balance-amount
            print(f"You withdrew {amount} and your total balance is {self.balance}")
            return self.balance
        else:
            return "You dont have sufficient balance"       
    
    def show_balance(self):
        return f"your Total balance as of now is: {self.balance}"
        
ram_account= BankAccount(123)  
print(ram_account.show_balance())
print(ram_account.deposit(700))
print(ram_account.withdraw(1300))

def add(self, other):
    self.numeratoer/ self. denominator + other.numeratoer/ other.denonminator

        