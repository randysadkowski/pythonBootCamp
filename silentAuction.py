from silentAuctionExtras import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}


def clear():
    print("\n" * 50)


def highest_bidder(bidder_record):
    highest_bid = 0
    winner = ""
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${bid}")


continue_auction = True
while continue_auction:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == "no":
        continue_auction = False
        highest_bidder(bids)
    elif more_bidders == "yes":
        clear()
