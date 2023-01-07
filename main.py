import alt_calc
#from replit import clear
#from art import logo
# #Calculator


# def calculate(num1, num2, function):
#     if function == "+":
#        return num1 + num2
    
#     elif function == "-":
#         return num1 - num2
    
#     elif function == "*":
#         return num1 * num2
    
#     elif function == "/":
#         return num1 / num2

# def run_calc():
#     print(logo)
#     num1 = int(input("Input first number: "))
#     function = input("Would you like to add '+', subtract '-', multiply '*', or divide '/': ")
#     num2 = int(input("Input seccond number: "))
#     result = calculate(num1=num1, num2=num2, function=function)
#     print(result)
#     action = input("Would you like to resume 'r', clear 'c', or quit 'q'? : ")
#     if action == "r":
#         re_calc(result)
#     elif action == "c":
#         clear()
#         run_calc()
#     elif action == "quit":
#         exit()

# def re_calc(result):
#     clear()
#     print(logo)
#     print(result)
#     function = input("Would you like to add '+', subtract '-', multiply '*', or divide '/': ")
#     num2 = int(input("Input number to calculate with previous result: "))
#     result = calculate(num1=result, num2=num2, function=function)
#     print(result)
#     action = input("Would you like to resume 'r', clear 'c', or quit 'q'? : ")
#     if action == "r":
#         re_calc(result)
#     elif action == "c":
#         clear()
#         run_calc()
#     elif action == "quit":
#         exit()

alt_calc.run_calc()