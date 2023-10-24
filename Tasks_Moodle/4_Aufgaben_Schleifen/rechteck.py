# Dieses Script erstellt ein Reckteck aus * Symbolen
# Überprüfung der Eingabe
cEingabe1 = True

while cEingabe1:
    zahlx = input("Geben Sie eine Anzahl an Spalten an: ")
    try: 
        zahlx = int(zahlx)
        cEingabe1 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

cEingabe2 = True

while cEingabe2:
    zahly = input("Geben Sie eine Anzahl an Reihen an: ")
    try: 
        zahly = int(zahly)
        cEingabe2 = False
    except:
        print("Geben Sie eine numerische Zahl ein.")
        print("Bitte versuchen Sie es erneut!")

for i in range(zahly, zahly*2+1):
    print(zahlx * "*")
    
# Torge's Lösung
# for _ in range(zahlx):
#     for _ in range(zahly):
#         print(end = "*")
#     print("\n")