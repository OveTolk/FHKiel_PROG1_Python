# Dieses Programm berechnet die Abschreibung pro Monat
# Überprüfung der Variablen
cEingabe1 = True
while cEingabe1:
    kosten = input("Geben Sie die Kosten an, die abgeschrieben werden sollen: ")
    try: 
        kosten = float(kosten)
        cEingabe1 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

cEingabe2 = True
while cEingabe2:
    monate = input("Geben Sie eine Anzahl an Monaten an, über die abgeschrieben werden soll: ")
    try: 
        monate = int(monate)
        cEingabe2 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

# Berechnung der Abschreibung pro Monat
apromonat = kosten / monate

# Ausgabe des Buchwerts
for i in range(1, monate + 1):
    kosten = kosten - apromonat
    print(f"Monat {i} Buchwert {kosten} € Abschreibung pro Monat {apromonat} €")