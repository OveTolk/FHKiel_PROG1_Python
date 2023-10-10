print("Dieses Programm errechnet den Zinseszins eines Anfangskapitals mit einem konstanten Zins und einer bestimmten Laufzeit.")
anfangskapital = float(input("Geben Sie das Anfangskapital (€) ein: "))
zinssatz = float(input("Geben Sie den Zinssatz (%) ein: "))
laufzeit = int(input("Geben Sie die Laufzeit (in Jahren): "))

nebenrechnung1 = zinssatz / 100 + 1
nebenrechnung2 = nebenrechnung1 ** laufzeit
endkapital = anfangskapital * nebenrechnung2
zinseszins = endkapital - anfangskapital

print(f"Mit einem Anfangskapital von {anfangskapital} € , einem Zinssatz von {zinssatz} % und einer Laufzeit von {laufzeit} Jahren ergibt sich ein Zinseszins von {round(zinseszins, 2)} €. Das Endkapital beträgt {round(endkapital, 2)} €.")