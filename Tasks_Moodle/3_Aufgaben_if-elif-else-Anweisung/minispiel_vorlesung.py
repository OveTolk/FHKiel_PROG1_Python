# Zufallsgeneratorspiel

import random
random.seed()

# Wert und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
ergebnis = a + b

zahl_abfragen = True
while zahl_abfragen:
    tipp = input(f"Was ist {a}+{b}? ")
    try:
        tipp = int(tipp)
        # An dieser Stelle hat die Umwandlung geklappt.
        zahl_abfragen = False
    except:
        print("Dies ist keine numerische Zahl.")
        print("Bitte versuche es erneut!")


if ergebnis == tipp:
    print("Das ist richtig!!")
else:
    print(f"Das war fallsch. Richtig wäre gewesen: {ergebnis}")