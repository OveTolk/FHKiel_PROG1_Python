# Erklärung was das Programm macht
print("Dieses Programm rechnet Celsius in Fahrenheit und umgekehrt.")

# Eingabe der benötigten Werte

wert = int(input("Geben Sie die Höhe der Temperatur an (ohne Einheit): "))
einheit = int(input("(1) Fahrenheit / (2) Celsius: "))

# Umrechnung der Werte in die andere Einheit + Ausgabe dieser Werte
if einheit == 1:
    nebenrechnung = wert - 32
    nebenrechnung2 = 5 / 9 
    umrechnung =  nebenrechnung2 * nebenrechnung
    print(f"{wert} F ist umgerechnet {round(umrechnung, 2)} °.")
elif einheit == 2:
    nebenrechnung  = 9 / 5 
    nebenrechnung2 = wert * nebenrechnung
    umrechnung = nebenrechnung2 + 32
    print(f"{wert} ° ist umgerechnet {round(umrechnung, 2)} F")