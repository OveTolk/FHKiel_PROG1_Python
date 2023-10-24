# Überprüfung der Eingabe
cEingabe1 = True

while cEingabe1:
    preis = input("Geben Sie den Preis (€) an: ")
    try: 
        preis = float(preis)
        cEingabe1 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

cEingabe2 = True

while cEingabe2:
    inflation = input("Geben Sie die Höhe der Inflation (%) an: ")
    try: 
        inflation = float(inflation)
        inflation = inflation / 100 + 1
        cEingabe2 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

cEingabe3 = True

while cEingabe3:
    jahre = input("Geben Sie die Anzahl an Jahre an, die berücksichtigt werden soll: ")
    try: 
        jahre = int(jahre)
        cEingabe3 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

for i in range(1, jahre +1):
    if inflation > 1.05:
        inflation = 1.05
        preis = preis * inflation
        print(f"Preis nach Jahr {i}: {round(preis, 2)} €")
    else:
        preis = preis * inflation
        print(f"Preis nach Jahr {i}: {round(preis, 2)} €")

print(f"Inflationsrate in Prozent: {round((inflation - 1) * 100)}")