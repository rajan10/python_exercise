def bid_info():    
    name=input("Enter your name: ")    
    bid_amount=int(input("Enter your bid amount: "))
    return name, bid_amount   

def get_max_amount_name(my_bidders_dict):
    temp_amount=0
    temp_name=""
    for name, bid_amount in my_bidders_dict.items():
        if bid_amount> temp_amount:
            temp_amount=bid_amount
            temp_name=name
    return temp_name, temp_amount    
  
def main():
    bidders ={}
    while True:
        name, bid_amount=bid_info()
        bidders[name]=bid_amount
          
        more_bidders =input("Do you have some more bidders? (Yes/No)").strip().lower()
        if more_bidders !='yes':
            break
        
    winner_name, winning_bid= get_max_amount_name(bidders)
    print(f" the winner is {winner_name} with the highest bid of ${winning_bid}!") 
       

    
if __name__== "__main__":
    main()




    
    