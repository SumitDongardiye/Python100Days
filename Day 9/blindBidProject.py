def find_highest_bidder(bidding_dictionary):
    max_value=0
    winner=""

    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>max_value:
            max_value=bid_amount
            winner=bidder
    
    print(f"The winner is {winner} with a bid of ${max_value}")

print("Welcome to the secret auction program.\n")
bid_dict={}

bidding=True

while bidding is True:
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    bid_dict[name]=bid
    game_continue=input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if game_continue=="no":
        bidding=False
        find_highest_bidder(bid_dict)

    else:
        print("\n"*20)



