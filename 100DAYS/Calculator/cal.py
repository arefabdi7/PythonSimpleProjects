from arts import ascii_cal, goodbye
from os import system


def cal(num1, num2, op):
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "Please  enter a valid operator"


flag = True
print(ascii_cal + "\n\n")

while True:
    if flag:
        num1 = float(input("What's the first number?: "))
    else:
        num1 = temp
    op = input("+\n-\n*\n/\nSelect an operation: ")
    num2 = float(input("What's the second number?: "))
    ans = cal(num1, num2, op)
    if isinstance(ans, str):
        print(ans)
        continue
    temp = float(ans)
    print(f"{num1} {op} {num2} = {temp}")
    cont = input(
        f"Do you want to continue with {ans} or restart calculator? or close app? (continue,restart,exit)\n"
    )
    match cont:
        case "continue":
            system("clear")
            flag = False
            continue
        case "restart":
            system("clear")
            flag = True
            continue
        case "exit":
            system("clear")
            print(goodbye)
            break
