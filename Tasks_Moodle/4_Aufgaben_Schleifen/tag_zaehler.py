# Dieses Programm prüft, wie viele Tage bis zu einem bestimmten Datum vergangen sind.

# Überprüfung der Eingabe
cEingabe1 = True

while cEingabe1:
    tag = input("Geben Sie den Tag an: ")
    try: 
        tag = int(tag)
        if (tag > 0) and (tag < 32):
                cEingabe1 = False
        else:
            print("Der Tag muss zwischen 1 und 31 liegen.")
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

cEingabe2 = True

while cEingabe2:
    monat = input("Geben Sie den Monat an: ")
    try: 
        monat = int(monat)
        if (monat > 0) and (monat < 13):
                cEingabe2 = False
        else:
            print("Der Monat muss zwischen 1 und 12 liegen.")
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

countDays = 0
# Berechnung der Tage
for i in range(1, monat):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        countDays += 31
    elif i == 2:
        countDays += 28
    else:
        countDays += 30
countDays += tag

# Ausgabe der Berechnung und Errormeldung
if tag > 28 and monat == 2:
     print("Führen Sie das Skript erneut aus. Der Februar kann nur 28 Tage haben.")
else:
    print(f"Tage sein Jahresanfang: {countDays}")



