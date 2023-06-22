import os
from secret_auction_art import logo

bids = {}
bidding_finished = False


def find_highest_bider(bid_record):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bid_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}")




print(logo)
print("Welcome to secret auction program\n")

while not bidding_finished:
    name = input("Enter your name : ")
    bid = int(input("Enter your bid price : $"))
    bids[name] = bid

    should_continue = input("Anyone else to bid, type 'yes' to continue or 'no' to exit : ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bider(bid_record=bids)
    elif should_continue == "yes":
        os.system("cls")
    else:
        print("\nEnter valid option")