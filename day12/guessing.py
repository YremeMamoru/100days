from random import randint

number = randint(1,100)

print("Welcome to the number guessing game!")
print("Try to guess a number between 1 and 100.")
print(f"Dev hint: the number is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
isValid = False

while not isValid:
    if difficulty == 'easy':
        attempts = 10
        isValid = True
    elif difficulty == 'hard':
        attempts = 5
        isValid = True
    else:
        print("Please, choose a valid option!")
        isValid = False

while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low!")
        attempts-=1
    elif guess > number:
        print ("Too high!")
        attempts-=1
    else:
        print(f"Congratulations! The number was {number}")
        exit()
    
print("You've run out of guesses, you lose.")