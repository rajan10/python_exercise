class Account:
    def __init__(self, name, balance, gender):  # total balace for male and female seperately
        # [Ram, Shyarm, Hair]  [Sita, Gita, Rita]
        self.name =name
        self.balance= balance
        self.gender= gender
  
def total_balance(*accounts): 
    female_sum=0
    male_sum=0
    male_account=[]
    female_account=[]
    for account in accounts:
        if account.gender=="Male":
            male_account.append(account.name)
            male_sum=male_sum+account.balance     
            
        else:
            female_account.append(account.name)
            female_sum=female_sum+account.balance
    return male_sum, male_account, female_sum, female_account

myaccount1=Account("Ram",100,"Male")
myaccount2=Account("Sita",200,"Female")
myaccount3=Account("Shayam",300,"Male")
myaccount4=Account("Gita",400,"Female")

male_sum,male_account,female_sum,female_account=total_balance(myaccount1,myaccount2,myaccount3,myaccount4)
print(f"Sum of balance of male is:{male_sum}")       
print(f"Sum of balance of female is:{female_sum}")
print(f"List of Male account: {male_account}")
print(f"List of Female account: {female_account}")

        
        
    

    
    
    

       