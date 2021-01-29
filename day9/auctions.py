import os
from platform import system
from assets import logo

clear = lambda: os.system("cls") if system() == "Windows" else os.system(
    "clear")
bidders_dict = {}


def main():
    highest_bid = 0
    winner = ""
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more == "yes" or more == "y":
        bidders_dict[name] = bid
        clear()
        main()
    else:
        for bidder, bid in bidders_dict.items():
            if bid > highest_bid:
                highest_bid = bid
                winner = bidder
        print(f"The winner is {winner} with a bid of {highest_bid}")


print(logo)
print("Welcome to the secret auction program.")
main()