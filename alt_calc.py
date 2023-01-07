from replit import clear
from art import logo
#Calculator

def add(num1, num2):
    result = num1 + num2
    return result
def subtract(num1, num2):
    result = num1 - num2
    return result
def multiply(num1, num2):
    result = num1 * num2
    return result
def divide(num1, num2):
    result = num1 / num2
    return result

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def run_calc():
    print(logo)
    num1 = float(input("Input first number: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the lines above: ")
    num2 = float(input("Input seccond number: "))
    result = operations[operation_symbol](num1=num1, num2=num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    action = input("Would you like to resume 'r', clear 'c', or quit 'q'? : ")
    if action == "r":
        re_calc(result)
    elif action == "c":
        clear()
        run_calc()
    elif action == "q":
        quit()

def re_calc(result):
    num1 = result
    clear()
    print(logo)
    print(result)
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the lines above: ")
    num2 = float(input("Input number to calculate with previous result: "))
    result = operations[operation_symbol](num1=result, num2=num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    action = input("Would you like to resume 'r', clear 'c', or quit 'q'? : ")
    if action == "r":
        re_calc(result)
    elif action == "c":
        clear()
        run_calc()
    elif action == "q":
        quit()

run_calc()