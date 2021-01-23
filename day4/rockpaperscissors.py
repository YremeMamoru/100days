from random import choice


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\n
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n
'''

user = input("What do you choose? [\"rock\", \"paper\", \"scissors\"]\n").lower()
option = choice([rock, paper, scissors])

if user == "rock":
    print(rock)
    print("Computer choose:\n")
    if option == rock:
        print(rock)
        print("It's a draw \n _")
    elif option == paper:
        print(paper)
        print("You lose \n _")
    else:
        print(scissors)
        print("You win \n _")
elif user == "paper":
    print(paper)
    print("Computer choose:\n")
    if option == rock:
        print(rock)
        print("You win \n _")
    elif option == paper:
        print(paper)
        print("It's a draw \n _")
    else:
        print(scissors)
        print("You lose \n _")
elif user == "scissors":
    print(scissors)
    print("Computer choose:\n")
    if option == rock:
        print(rock)
        print("You lose \n _")
    elif option == paper:
        print(paper)
        print("You win \n _")
    else:
        print(scissors)
        print("It's a draw \n _")
else:
    print("choose a valid option!")
    print('''
   __
  (__)
  |()| 
 _|()|_ _
(()()()())
(        |
(        |
 \      /
  |     |''')
