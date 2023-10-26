# Dieses Programm überprüft, ob es sich bei der eingegeben Zahl um eine Primzahl handelt.

# User-Input
def userInput():
    # Überprüfung der Eingabe
    cEingabe1 = True
    while cEingabe1:
        zahl = input("Geben Sie die zu überprüfende Zahl an: ")
        try: 
            zahl = int(zahl)
            cEingabe1 = False
        except:
            print("Geben Sie eine numerische Zahl ein.")
            print("Bitte versuchen Sie es erneut!")
    return zahl

def checkPrimzahl(zahl):
    # Wert für While-Schleife
    check = True

    # Für spätere Beantwortung, ob Zahl Primzahl
    teiler = 0
    ergebnis = 0

    # While-Schleife, die überprüft, ob Zahl durch weitere Zahl teilbar ist.
    while check:
        for i in range(2, zahl):
            result = zahl / i
            if result in range(2, zahl):
                teiler = i
                ergebnis = result
                check = False
            else:
                check = False
    # Ausgabe, ob Primzahl
    if teiler == 0 and ergebnis == 0:
        print(f"Bei der Zahl {zahl} handelt es sich um eine Primzahl.")
    else:
        print(f"Bei {zahl} handelt es sich um keine Primzahl. Grund:")
        print(f"Zahl    : {zahl}")
        print(f"Quotient: {teiler}")
        print(f"Ergebnis: {int(ergebnis)}")
# Hauptprogramm
def main():
    print("Dieses Programm gibt aus, ob die zu überprüfende Zahl des Users eine Primzahl ist.")
    zahl = userInput()
    checkPrimzahl(zahl)

main()