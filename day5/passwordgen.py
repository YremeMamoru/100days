import string
import random

passlist = []

print("Bem vindo ao gerador de senhas Python")
letters = int(input("Quantas letras você quer em sua senha? \n"))
symb = int(input("Quantos simbolos você quer em sua senha? \n"))
numbers = int(input("Quantos números você quer em sua senha? \n"))

for i in range(0, letters):
    passlist.append(random.choice(string.ascii_letters))
for i in range(0, symb):
    passlist.append(random.choice(string.punctuation))
for i in range(0, numbers):
    passlist.append(random.choice(string.digits))

random.shuffle(passlist)

passtr = ''.join(passlist)
print(f'Your password is: {passtr}')