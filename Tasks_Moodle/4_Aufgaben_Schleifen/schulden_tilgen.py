# Dieses Programm prüft, wie lange es dauert einen Schuldbetrag bei einer bestimmten Höhe von Zinsen und Tilgung zurückbezahlt.

# Überprüfung der Eingabe
cEingabe1 = True

while cEingabe1:
    schulden = input("Geben Sie die Höhe der Schulden (€) an: ")
    try: 
        schulden = float(schulden)
        cEingabe1 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

cEingabe2 = True

while cEingabe2:
    tilgung = input("Geben Sie die Höhe der Tilgung (€) an: ")
    try: 
        tilgung = float(tilgung)
        cEingabe2 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

cEingabe3 = True

while cEingabe3:
    zinsen = input("Geben Sie die Höhe der Zinsen (%) an: ")
    try: 
        zinsen = float(zinsen)
        zinsen = zinsen / 100 + 1
        cEingabe3 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

# Berechnung der Monate und der Schuldbeträge
monat = 0
while not schulden < 0:
    schulden -= tilgung
    schulden *=  zinsen
    monat = monat + 1
    print(f"Im Monat {monat} liegen die Schulden bei {round(schulden, 2)} €.")
