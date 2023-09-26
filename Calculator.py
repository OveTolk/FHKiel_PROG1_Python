number1 = input("Zahl 1: ")
method = input("Wähle: + - * / : ")
number2 = input("Zahl 2: ")


if method == "+":
    result = int(number1) + int(number2)
elif method == "-":
    result = int(number1) - int(number2)
elif method == "*":
    result = int(number1) * int(number2)
elif method == "/":
    result = int(number1) / int(number2)

print(result)