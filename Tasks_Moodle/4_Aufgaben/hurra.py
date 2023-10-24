# Dieses Programm gibt ein Wort zahl-mal nacheinander aus.

# User-Input des Worts
text = input("Geben Sie ein Wort ein: ")

# Überprüfung der Eingabe
cEingabe = True

while cEingabe:
    zahl = input("Geben Sie eine Anzahl ein, wie oft das Wort wiederholt werden soll: ")
    try: 
        zahl = int(zahl)
        cEingabe = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

# Output
for i in range(1, zahl + 1):
    print(text)
