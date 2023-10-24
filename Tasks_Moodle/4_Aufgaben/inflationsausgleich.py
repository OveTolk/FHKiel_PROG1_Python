# Überprüfung der Eingabe
cEingabe1 = True

while cEingabe1:
    preis = input("Geben Sie die Höhe der Schulden (€) an: ")
    try: 
        Preis = float(Preis)
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