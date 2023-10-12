# Erklärung was das Programm macht
print("Dieses Programm rechnet Celsius in Fahrenheit und umgekehrt.")

# Eingabe der benötigten Werte

wert = int(input("Geben Sie die Höhe der Temperatur an (ohne Einheit): "))
einheit = int(input("(1) Fahrenheit / (2) Celsius: "))

# Umrechnung der Werte in die andere Einheit + Ausgabe dieser Werte
if einheit == 1:
    umrechnung = (wert - 32) * (5 / 9)
    print(f"{wert} F ist umgerechnet {round(umrechnung, 2)} °.")
elif einheit == 2:
    umrechnung = (wert * (9 / 5)) + 32
    print(f"{wert} ° ist umgerechnet {round(umrechnung, 2)} F")