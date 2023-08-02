class Account:
    def __init__(self, name, balance):
        self.name =name
        self.balance= balance
    
def summation(*args):
    sum=0
    for number in args:
        sum=sum+number
    return sum
#(myaccount1, myacount2)
def total_balance(*accounts): 
    sum=0
    for account in accounts:
        sum=sum+account.balance
    return sum

myaccount1=Account("my_account1",100)
myaccount2=Account("my_account2",200)
myaccount3=Account("my_account3",300)

result=total_balance(myaccount1,myaccount2,myaccount3)
print(result)


        
        
    

    
    
    

       