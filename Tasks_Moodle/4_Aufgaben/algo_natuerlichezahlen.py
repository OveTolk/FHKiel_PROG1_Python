# Dieses Programm merkt sich die größte eingegebene Zahl. Bei der ersten falschen Eingabe, wird die Zahl ausgegeben.

# Defintion der Variable, um die später zu verändern.
zahl = 0

# Verarbeitung der User Inputs
cEingabe = True
while cEingabe:
    zahlneu = input("Geben Sie eine natürliche Zahl ein: ")
    try:
        zahlneu = int(zahlneu)
        if zahlneu > zahl:
            zahl = zahlneu
    except:
        cEingabe = False

# Ausgabe der größten Zahl
print(f"Die größte eingegebene Zahl ist: {zahl} gewesen.")