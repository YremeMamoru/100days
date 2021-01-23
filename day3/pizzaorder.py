conta = 0
print("bem vindo a pizzaria ffodase")
tamanho = input("fala o tamanho de pizza que você quer [S, M, L]: ")
print(tamanho.upper())

if tamanho.upper() == 'S':
  conta += 15
elif tamanho.upper() == 'M':
  conta += 20
elif tamanho.upper() == 'L':
  conta += 25
else:
  print("por favor, selecione um tamanho válido")
  exit()

pepes = input("tu quer peperone ? [S, N]: ")

if pepes.upper() == 'S':
  if tamanho.upper() == 'S':
    conta += 2
  else:
    conta += 3

quejin = input("tu quer queijo extra? ? [S, N]: ")
 
if quejin.upper() == "S":
  conta += 1

print(f"o valor da conta é {conta}")