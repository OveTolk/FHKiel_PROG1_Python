# Dieses Programm berechnet den Gewinn anhand des Umsatzes und der Kosten

# Eingabe
umsatz = float(input("Geben Sie den Umsatz (€) ein: "))
kosten = float(input("Geben Sie die Kosten (€) ein: "))

# Verarbeitung
gewinn = umsatz - kosten

# Ausgabe
if gewinn < 0:
    print(f"Der Verlust beträgt {round(gewinn, 2)} €.")
elif gewinn == 0:
    print(f"Es liegt weder ein Gewinn noch ein Verlust vor.")
else:
    print(f"Der Gewinn beträgt {round(gewinn, 2)} €.")