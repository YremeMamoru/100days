import string
from assets import logo

alphabet = list(2 * string.ascii_lowercase)


def caesar(text, shift, direction):
    message = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            cyphIndex = alphabet.index(char) + shift
            message += alphabet[cyphIndex]
        else:
            message += char
    return message


def main():
    isValid = False
    while not isValid:
        direction = input(
            'Type "enconde" to encrypt, type "decode" to decript: \n').lower()
        if direction not in ['encode', 'decode']:
            print("Please choose a valid option")
        else:
            isValid = True
    text = input("Type the message: \n")
    shift = int(input("Type the shift number: \n")) % 26
    print(f"the message is: {caesar(text, shift, direction)}")
    restart = input("Do you want to restart? [Yes/No]:\n ").lower()
    if restart == "yes" or restart == "y":
        main()
    else:
        print("Goodbye.")


#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'.
print(logo)
main()
