# Erklärung was das Programm macht.
print("Dieses Programm berechnet den sogenannten Break-Even-Punkt.")
print("Der Break-Even-Punkt ist der Punkt, ab welcher Stückzahl an verkauften Produkten ein Produkt rentabel ist.")

# User Input für Variablen
fix = float(input("Bitte geben Sie die Fixkosten ein: "))
variabel = float(input("Bitte geben Sie die variablen Kosten (pro Produkt) ein: "))
preis = float(input("Bitte geben Sie den Verkaufspreis pro Produkt ein: "))

# Berechnung des Break-Even-Points

breakeven = fix / (preis - variabel)

print(f"Ab {round(breakeven, 2)} verkauften Produkten ist das Produkt rentabel und kann so einen Gewinn erzielen.")