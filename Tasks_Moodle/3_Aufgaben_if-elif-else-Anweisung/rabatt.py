# Dieses Programm berechnet den Rabatt nach der Bestellgröße des Inputs

# Prüfen ob Eingabe aus Ints besteht und Bestellwert > 0
eingabe = True
while eingabe:
    bestellung = input("Geben Sie den Wert (€) der Bestellung an: ")
    try:
        bestellung = float(bestellung)
    except:
        print("Dies ist keine numerische Zahl.")
        print("Bitte versuche es erneut!")
    if bestellung > 0:
        eingabe = False
    else:
        print("Der Wert der Bestellung muss größer sein als 0 €.")

# Rabatt Variablen erstellen rabat0 für 0%, rabatt5 für 5%
rabatt0 = 100
rabatt5 = 499

# Berechnung des Rabatts anhand des Werts der Bestellung
if bestellung < rabatt0:
    aktion = bestellung * 0.05
    bestellungneu = bestellung - aktion
    print(f"Bestellwert: {bestellung} €")
    print(f"Sie erhalten einen Rabatt von: {aktion} €.")
    print(f"Der Rabatt bei einer Bestellung unter {rabatt0} beträgt 0%. Daher liegen die Kosten der Bestellung bei {bestellungneu} €.")
elif (bestellung >= rabatt0) and (bestellung <= rabatt5):
    aktion = bestellung * 0.05
    bestellungneu = bestellung - aktion
    print(f"Bestellwert: {bestellung} €")
    print(f"Sie erhalten einen Rabatt von: {aktion} €.")
    print(f"Der Rabatt der Bestellung bei {rabatt0} € oder mehr liegt bei 5%. Daher liegen die Kosten der Bestellung bei {bestellungneu} €")
elif bestellung > rabatt5:
    aktion = bestellung * 0.10
    bestellungneu = bestellung - aktion
    print(f"Bestellwert: {bestellung} €")
    print(f"Sie erhalten einen Rabatt von: {aktion} €.")
    print(f"Der Rabatt der Bestellung bei über {rabatt5} € liegt bei 10%. Daher liegen die Kosten der Bestellung bei {bestellungneu} €")
else:
    print("Fehler im Programm.")