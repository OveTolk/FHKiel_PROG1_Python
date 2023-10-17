# Dieses Programm berechnet den zustehenden Bonus eines Mitarbeiters gemessen am Erfolg des Unternehmens

# Prüfen ob Eingabe aus Ints besteht und Umsatz > 0
eingabe = True
while eingabe:
    umsatz = input("Geben Sie den Umsatz (€) des Unternehmens an: ")
    try:
        umsatz = float(umsatz)
    except:
        print("Dies ist keine numerische Zahl.")
        print("Bitte versuche es erneut!")
    if umsatz > 0:
        eingabe = False
    else:
        print("Der Wert der Umsatzes muss größer sein als 0 €.")

# Bestimmen der Grenzen des Bonus
umsatzgrenze1 = 50000
bonus5prozent = 0.05
bonus10prozent = 0.1
umsatzgrenze2 = 100000

if umsatz < umsatzgrenze1:
    print(f"Der Umsatz des Unternehmens liegt bei {umsatz} €.")
    print(f"Da der Umsatz des Unternehmens unter {umsatzgrenze1} liegt, wird dem Mitarbeiter kein Bonus gezahlt.")
elif (umsatz >= umsatzgrenze1) and (umsatz <= umsatzgrenze2):
    bonus = (umsatz - umsatzgrenze1) * bonus5prozent
    print(f"Der Umsatz des Unternehmens liegt bei {umsatz} €.")
    print(f"Da der Umsatz über der Umsatzgrenze von {umsatzgrenze1} € liegt, wird ein Bonus von 5% gezahlt.")
    print(f"Der Bonus für die Mitarbeiter beträgt: {bonus} €.")
elif umsatz > umsatzgrenze2:
    bonus1 = (umsatzgrenze2 - umsatzgrenze1) * bonus5prozent
    bonus2 = (umsatz - umsatzgrenze2) * bonus10prozent
    bonusges = bonus1 + bonus2
    print(f"Der Umsatz des Unternehmens liegt bei {umsatz} €.")
    print(f"Da der Umsatz über der Umsatzgrenze von {umsatzgrenze2} € liegt, wird zwischen {umsatzgrenze1} € und {umsatzgrenze2} € ein Bonus von 5% gezahlt.")
    print(f"Auf den Umsatz über {umsatzgrenze2} € wird ein Bonus von 10 % gezahlt. Daher wird ein Gesamtbonus von {bonusges} € gezahlt.")
else: 
    print("Es liegt ein Fehler vor.")