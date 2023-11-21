
wochen_preise = [10, 12, 15, 9, 8, 14, 13, 11, 15, 16]
schwellenwert = 12

anzahl = 0

for i in wochen_preise:
    if i > schwellenwert:
        anzahl = anzahl + 1

print(f"Der Wert liegt {anzahl} Mal über dem Schwellenwert {schwellenwert}")