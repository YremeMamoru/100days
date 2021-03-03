import random
from assets import logo
import numpy as np

 ############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game: 
  # https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here: 
# http://blackjack-final.appbrewery.repl.run
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playercards = np.array([])
dealercards = np.array([])

play = input("Do you want to play blackjack? [y/n]").lower()


while play == ' y':
    print(logo)
    for i in range(0,1):
        playercards.append(random.choice(cards))
        dealercards.append(random.choice(cards))
    currentscore = np.sum(playercards)
    print(f'Your cards: {playercards}, current score: {currentscore}')
    
