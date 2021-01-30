import os
from platform import system
from assets import logo

clear = lambda: os.system("cls") if system() == "Windows" else os.system(
    "clear")
result = 0


def calc(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        clear()
        print(logo)
        return "Invalid operation"


def main(cont="n"):
    result = 0
    if cont != "y":
        first = int(input("What's the first number?: "))
    else:
        first = result
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    second = int(input("What's the next number?: "))
    result = calc(first, second, operation)
    if result == "Invalid operation":
        print(result)
        main()
    else:
        print(f"{first} {operation} {second} = {result}")
        cont = input(
            f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: "
        ).lower()
        if cont == "y":
            main(cont)
        else:
            clear()
            print(logo)
            main(cont)


clear()
print(logo)
main(cont="n")
