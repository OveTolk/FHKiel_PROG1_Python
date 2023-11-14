# Monatlicher Umsatz in höchsten, niedrigsten und durchschnittlichen Umsatz berechnen

# Nutzereingabe der monatlichen Umsätze
def monat_umsatz():
    umsatz = []
    for i in range(1, 13):
        monat = float(input(f"Geben Sie den Umsatz für den Monat {i} an: "))
        umsatz.append(monat)
    return umsatz

# Berechnung des durchschnittlichen Umsatzes
def avg_wert(list):
    gesamt = 0
    for i in list:
        gesamt+=i
    anzahl = len(list)
    avg = gesamt/anzahl
    return round(avg, 2)

# Bestimmung des höchsten und niedrigsten Umsatzes
def high_low(list):
    high = 0
    low = list[0]
    for i in list:
        if i > high:
            high = i
        elif i < low:
            low = i
        else:
            pass
    return high, low
        
# Hauptschleife
def main():
    list_umsatz = monat_umsatz()
    avg = avg_wert(list_umsatz)
    high, low = high_low(list_umsatz)
    print(f"Höchster Umsatz des Jahres: {high} Euro.")
    print(f"Niedrigster Umsatz des Jahres: {low} Euro.")
    print(f"Durchschnittlicher Umsatz des Jahres: {avg} Euro.")

# Ausführung
main()