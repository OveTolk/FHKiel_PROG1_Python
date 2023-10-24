#Wiederholung von der 3. Vorlesung
zielbetrag = 699
sparbetrag = 0
zinsen = 1.01
i = 0
einzahlung = 1

while sparbetrag <= zielbetrag:  
    sparbetrag += einzahlung
    sparbetrag = sparbetrag * zinsen
    i += 1
    print(f"Monat {i} Sparbetrag {round(sparbetrag, 2)} €")

zinsertrag = (sparbetrag - (i * einzahlung))
print(f"Nach {i} Monaten sind Zinsen von {round(zinsertrag, 2)} € zustandegekommen.")