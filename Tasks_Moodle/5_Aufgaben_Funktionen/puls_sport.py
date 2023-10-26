# Dieses Programm berechnet den perfekten Puls bei Ausdauersportarten anhand des Alters

# User-Input des Alters
def userInput():
    alter = input("Geben Sie Ihr Alter an: ")
    return int(alter)

# Berechnung des perfekten Pulses
def calcPerfectPuls(alter):
    puls = 165 - (0.75*alter)
    return puls

# Ausgabe im Terminal
def output(alter, puls):
    print(f"Alter           : {alter}")
    print(f"Optimaler Puls  : {puls}")

# Haupt-Programm
def main():
    alter = userInput()
    perfPuls = calcPerfectPuls(alter)
    output(alter, perfPuls)

main()