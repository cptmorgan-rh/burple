import os

auction_dict = {}

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction_dict[name] = bid
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if add_bidders != "yes":
        break
    os.system('clear')

highest_bid = 0
winning_bidder = ""

for x in list(auction_dict.keys()):
    if auction_dict[x] > highest_bid:
        winning_bidder = x
        highest_bid = auction_dict[x]

print(f"{winning_bidder} won with a bid of {highest_bid}")
