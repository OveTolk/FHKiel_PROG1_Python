# Dieses Programm errechnet den Preisnachlass bei einem bestimmten Preis und Rabatt.

preis = float(input("Geben Sie den alten Preis (€) an: "))
rabatt = float(input("Geben Sie den Rabatt (%) an: "))

neuerpreis = preis * (1 - rabatt / 100)
nettorabatt = preis - neuerpreis

print(f"Das Produkt mit einem Verkaufspreis von {preis} € kostet mit einem Rabatt von {rabatt} % noch {round(neuerpreis, 2)} €.")
print(f"Der Nettobetrag des Rabatts liegt so bei {round(nettorabatt, 2)} €.")