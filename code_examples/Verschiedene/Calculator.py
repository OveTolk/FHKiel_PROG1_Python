# Simple calculator based on user inputs

number1 = input("Number 1: ")
method = input("Choose: + - * / : ")
number2 = input("Number 2: ")

if method == "+":
    result = int(number1) + int(number2)
elif method == "-":
    result = int(number1) - int(number2)
elif method == "*":
    result = int(number1) * int(number2)
elif method == "/":
    result = int(number1) / int(number2)

print(result)