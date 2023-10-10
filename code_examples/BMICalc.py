height = input("Input height (in cm): ")
weight = input("Input weight (in kg): ")

height = int(height)
height = height / 100
weightint = int(weight)
height2 = height ** 2
bmi = weightint / height2

underweight = 18.5
normalweight = 24.9
preadipositas = 29.9
moderateadipositas = 34.9
strongadipositas = 39.9
user_score = ""

if bmi < underweight:
    user_score = "Underweight"
elif ((bmi > underweight) and (bmi < normalweight)):
    user_score = "Normalweight"
elif ((bmi < preadipositas) and (bmi > normalweight)):
    user_score = "Overweight"
elif ((bmi > normalweight) and (bmi < preadipositas)):
    user_score = "Pre-adipositas"
elif ((bmi > preadipositas) and (bmi < moderateadipositas)):
    user_score = "Moderate adipositas"  

print(f"Your height is {height} m. Your weight is {weight} kg. Your calculated BMI is {round(bmi, 2)} - {user_score}.")