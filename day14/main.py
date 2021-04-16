import os
from random import choice, randint
from platform import system
from assets import logo, vs, data


clear = lambda: os.system("cls") if system() == "Windows" else os.system(
    "clear")

def showlogo():
    clear()
    print(logo)

def formatData(account):
    return f"{account['name']}, a {account['description']} from {account['country']}"

def game():
    gameOver = False
    score = 0
    
    while not gameOver:
        showlogo()
        if score > 0:
            print(f"You're right! Current score: {score}.")
        
        
        a = []
        b = []
        while a == b: 
            a = choice(data)
            b = choice(data)
        

        if a["follower_count"] > b["follower_count"]:
            winner = 'a'
        else:
            winner = 'b'

        print(f"Compare A: {formatData(a)}")
        print(vs)
        print(f"Against B: {formatData(b)}")
        userchoice = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        
        if userchoice == winner:
            score += 1
        else:
            showlogo()
            print(f"Sorry, that's wrong. Final score: {score}.")
            gameOver = True

game()