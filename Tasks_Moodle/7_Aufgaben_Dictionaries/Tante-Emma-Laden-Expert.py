warenlager = {}
listBestellungen = {}
def addProdukte(produkt):
    warenlager[produkt[0]] = produkt[1]

def inputAddProdukt():
    print("Hier fügen Sie ein neue Produkte hinzu.")
    check = True
    while check:
        name = input("Geben Sie den Namen des Produkts ein: ")
        preis = input("Geben Sie den Preis des Produkts ein: ")
        list = [name, preis]
        addProdukte(list)
        more = input("Möchten Sie ein weiteres Produkt hinzufügen? [Ja / Nein]: ")
        if more == "Nein":
            return
        else:
            pass

def inputBestellanzahl(warenlager):
    for i, value in warenlager.items():
        listBestellungen[i] = input(f"Wie viele {i} möchtest Du zum Preis {value} kaufen: ")

def calcPreis(warenlager, listBestellungen):
    gesPreis = 0
    list = []
    for name, preis in warenlager.items():
        anzahl = listBestellungen[name]
        preis = int(anzahl) * int(preis)
        gesPreis = gesPreis + preis   
    return gesPreis

def main():
    inputAddProdukt()
    inputBestellanzahl(warenlager)
    gesPreis = calcPreis(warenlager, listBestellungen)
    print(f"Der Gesamtpreis der Bestellung liegt bei {gesPreis} €")

main()