height = input("Input height (in cm): ")
weight = input("Input weight (in kg): ")

height = int(height)
height = height / 100
weightint = int(weight)
height2 = height ** 2
bmi = weightint / height2

print(round(bmi, 2))