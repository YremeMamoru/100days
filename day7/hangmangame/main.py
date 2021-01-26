import random
import os
from platform import system
from assets import word_list, stages, logo

clear = lambda: os.system('cls') if system() == "Windows" else os.system(
    'clear')

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

#Create blanks
display = []
guessed_letters = []
for letter in chosen_word:
    display += '_'

clear()
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter

    clear()

    if guess not in chosen_word and guess not in guessed_letters:
        lives -= 1
    elif guess in guessed_letters and guess not in chosen_word:
        print("Gonna miss again?")
    elif guess in guessed_letters:
        print("You already guessed this letter")

    guessed_letters += guess

    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print("You lose")
