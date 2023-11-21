
# Waren-Endpreise
warenlager = {'Butter': 1.90,
 'Brot': 2.30,
 'Schokolade': 1.50,
 'Apfel': 1.20}

def inputLager():
    lagerButter = int(input("Geben Sie die Anzahl an Butter an: "))
    lagerBrot = int(input("Geben Sie die Anzahl an Brot an: "))
    lagerSchokolade = int(input("Geben Sie die Anzahl an Schokolade an: "))
    lagerApfel = int(input("Geben Sie die Anzahl an Apfel an: "))
    list = [lagerButter, lagerBrot, lagerSchokolade, lagerApfel]
    return list

def abfrageWarenwert(list):
    wertButter = list[0] * warenlager['Butter']
    wertBrot = list[1] * warenlager['Brot']
    wertSchokolade = list[2] * warenlager['Schokolade']
    wertApfel = list[3] * warenlager['Apfel']
    wertList = [wertButter, wertBrot, wertSchokolade, wertApfel]
    return wertList

def gesamtpreis(warenwert):
    gesPreis = 0
    for i in warenwert:
        gesPreis = gesPreis + i
    return gesPreis

def main():
    lager = inputLager()
    warenwert = abfrageWarenwert(lager)
    gesPreis = gesamtpreis(warenwert)
    print(f"Gesamtpreis         : {round(gesPreis, 2)} €")
    print("Positionen")
    print(f"Butter              : {round(warenwert[0], 2)} €")
    print(f"Brot                : {round(warenwert[1], 2)} €")
    print(f"Schokolade          : {round(warenwert[2], 2)} €")
    print(f"Apfel               : {round(warenwert[3], 2)} €")

main()