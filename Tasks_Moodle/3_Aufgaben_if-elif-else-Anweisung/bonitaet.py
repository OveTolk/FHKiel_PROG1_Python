# Dieses Programm überprüft, ob ein Unternehmen Kreditwürdig ist.

# Prüfen ob Eingabe aus Ints besteht
eingabe = True
while eingabe:
    einkommen = input("Geben Sie das monatliche Einkommen des Unternehmens an: ")
    ausgaben = input("Geben Sie die monatlichen Ausgaben des Unternehmens an: ")
    try:
        einkommen = float(einkommen)
        ausgaben = float(ausgaben)
        eingabe = False
    except:
        print("Dies ist keine numerische Zahl.")
        print("Bitte versuche es erneut!")

# Berechnung und Ausgabe des Status der Bonität
if (einkommen * 2) >= ausgaben:
    print("Der Kunde ist Kreditwürdung.")
else:
    print("Der Kunde ist nicht kreditwürdig.")