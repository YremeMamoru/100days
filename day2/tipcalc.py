print("Bem vindo à calculadora de gorgeta.")
total = float(input("Qual foi o total da conta? R$"))
pessoas = int(input("Quantas pessoas dividirão a conta? "))

valid = [10,12,15]
porc = 0

while porc not in valid:
  porc = int(input("Qual a porcentagem de gorgeta você gostaria de dar? 10, 12 ou 15? "))
  if porc not in valid:
    print("Escolha um valor válido")

conta = round(((1 + porc/100)*total)/pessoas,2)
print(f"Cada pessoa deve pagar R${conta} ")