# Erklärung was das Programm macht
print("Dieses Programm errechnet den Zinseszins eines Anfangskapitals mit einem konstanten Zins und einer bestimmten Laufzeit.")

# Bestimmung der benötigten Eingaben
anfangskapital = float(input("Geben Sie das Anfangskapital (€) ein: "))
zinssatz = float(input("Geben Sie den Zinssatz (%) ein: "))
laufzeit = int(input("Geben Sie die Laufzeit (in Jahren): "))

# Berechnungen der Werte
nebenrechnung1 = zinssatz / 100 + 1
nebenrechnung2 = nebenrechnung1 ** laufzeit
endkapital = anfangskapital * nebenrechnung2
zinseszins = endkapital - anfangskapital

# Ausgabe der Werte
print(f"Mit einem Anfangskapital von {anfangskapital} € , einem Zinssatz von {zinssatz} % und einer Laufzeit von {laufzeit} Jahren ergibt sich ein Zinseszins von {round(zinseszins, 2)} €. Das Endkapital beträgt {round(endkapital, 2)} €.")