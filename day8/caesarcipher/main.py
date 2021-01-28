import string

alphabet = list(2 * string.ascii_lowercase)


def caesar(text, shift, direction):
    message = ""
    for char in text:
        if char in alphabet:
            if direction == "decode":
                shift *= -1
            cyphIndex = alphabet.index(char) + shift
            message += alphabet[cyphIndex]
        else:
            message += char
    return message


isValid = False
while not isValid:
    direction = input(
        'Type "enconde" to encrypt, type "decode" to decript: \n').lower()
    if direction not in ['encode', 'decode']:
        print("Please choose a valid option")
    else:
        isValid = True

text = input("Type the message: \n")
shift = int(input("Type the shift number: \n"))

print(caesar(text, shift, direction))
