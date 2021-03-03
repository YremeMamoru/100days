import random
import os
from platform import system
from assets import logo

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

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")

def dealCard():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculateScore(cardList):
  if len(cardList) == 2 and sum(cardList) == 21:
    return 0
  if sum(cardList) > 21 and 11 in cardList:
    cardList.remove(11)
    cardList.append(1)
  return sum(cardList)

def compare(userScore, dealerScore):
  if userScore > 21 and dealerScore > 21:
    return "You went over. You lose!"

  if userScore == dealerScore:
    return "Draw!"    
  elif dealerScore == 0:
    return "You lose, your opponent has a blackjack!"
  elif userScore == 1:
    return "You win with a blackjack!"
  elif userScore > 21:
    return "You went over. You lose!"
  elif dealerScore > 21:
    return "The dealer went over, you win!"
  elif userScore > dealerScore:
    return "You win!"
  else:
    return "You lose!"


def game():
  print(logo)
  playercards = []
  dealercards = []
  gameover = False
  for i in range(0,2):
    playercards.append(dealCard())
    dealercards.append(dealCard())
  
  while not gameover:
    currentscore = calculateScore(playercards)
    dealerscore = calculateScore(dealercards)
    print(f'Your cards: {playercards}, current score: {currentscore}')
    print(f'Computer first card: {dealercards[1]}')
    
    if currentscore == 0 or dealerscore == 0 or currentscore > 21:
      gameover = True
    else:
      choice = input("Want to draw another card? [y/n]: ").lower()
      if choice == 'y':
        playercards.append(dealCard())
      else:
        gameover = True
      
  while dealerscore != 0 and dealerscore < 17:
    dealercards.append(dealCard())
    dealerscore = calculateScore(dealercards)
    
  print(f"Your hand: {playercards}. Final score : {currentscore}.")
  print(f"Dealer hand: {dealercards}. Dealer final score: {dealerscore}.")
  print(compare(currentscore, dealerscore))


play = input("Do you want to play blackjack? [y/n]: ").lower()
while play == 'y':
  clear()
  game()
  play = input("Do you want to play blackjack? [y/n]: ").lower()