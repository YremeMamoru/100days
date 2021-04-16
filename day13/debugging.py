############DEBUGGING#####################

# # Describe Problem
# This function iterates an 'i' variable in the range from 1 to 20, and when 'i' reaches 20, it prints "You got it".
# The bug is that the program does not prints nothing, when it should print after the range is fully iterated.
# The solution is that actually, the python method "range" stop argument is ommited, therefore, the range(i,j) creates a number in the range between i and j-1
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# This function is a dice roller that reproduces one of the dice images in the list, randomly
# The bug is that ocasionally, an IndexError occurs, telling that the list index is out of range.
# Furthermore, it looks like the '1' never is selected from the dice
# The bug occurs because the index for lists in python starts from 0, thus, it is impossible to found an item from the list where the index is '6', because it stops on 5.
# There is two solutions for the bug: subtract 1 from the index on the print function, or change the randint from 0 to 5
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6)
# # print(dice_num)
# print(dice_imgs[dice_num-1])

# Play Computer
# This function tells your generation based on the year inserted by the user.
# The bug is that nothing shows on the screen when it is inserted the year 1994
# The cause of the bug is because the if statement doesn't include the year 1994 as an option, just the range between 1980 and 1994, not including both, and after 1994
# The solution for the bug is to include the 1994 adding an equal sign next to the bigger or lesser sign 
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# Three bugs in the code: the IdentationError that can be solved adding a tab before the print function, and the TypeError, that can be solved converting the age input to an integer.
# And finally, a bug that doesn't show the variable age, that can be solved simply putting a 'f' letter before the string where it could be formatted
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# Print is Your Friend
# The bug occurs in the second input, where is used an equality signal instead of an assign signal
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# print(pages)
# word_per_page = int(input("Number of words per page: "))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])