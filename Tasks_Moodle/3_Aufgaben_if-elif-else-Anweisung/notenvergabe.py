# Berechnung der Schulnoten anhand externe Einflüsse.

import math

# Prüfen ob Eingabe richtig
eingabe = True
while eingabe:
    eingabenote = True
    while eingabenote:
        note = input("Geben Sie die objektive Note der Schüler:in an (1-6): ")
        try:
            note = float(note)
            if (note > 0) and (note < 7):
                eingabenote = False
            else:
                print("Die Note muss eine Zahl von 1-6 sein.")
        except:
            print("Dies ist keine numerische Zahl.")
            print("Bitte versuche es erneut!")

    eingabeauge = True
    while eingabeauge:
        auge = input("Geben Sie die Augenfarbe der Schüler:in an (dunkel: 1 und hell: 0): ")
        try:
            auge = int(auge)
            if (auge >= 0) and (auge <= 1):
                eingabeauge = False
            else:
                print("Bitte wähle die Augenfarbe erneut aus. Für hell: 0 und dunkel: 1")
        except:
            print("Dies ist keine numerische Zahl.")
            print("Bitte versuche es erneut!")
            
    eingabefrisur = True
    while eingabefrisur:
        frisur = input("Geben Sie die Frisur der Schüler:in an (kurz: 1 und lang: 0): ")
        try:
            frisur = int(frisur)
            if (frisur >= 0) and (frisur <= 1):
                eingabefrisur = False
            else:
                print("Bitte wähle die Frisur erneut aus. Für lang: 0 und kurz: 1")
        except:
            print("Dies ist keine numerische Zahl.")
            print("Bitte versuche es erneut!")

    eingabewetter = True
    while eingabewetter:
        wetter = input("Geben Sie das heutige Wetter an.(schön: 1 und nicht schön: 0): ")
        try:
            wetter = int(wetter)
            if (wetter >= 0) and (wetter <= 1):
                eingabewetter = False
            else:
                print("Bitte wähle das Wetter erneut aus. Für schön: 1 und nicht schön: 0")
        except:
            print("Dies ist keine numerische Zahl.")
            print("Bitte versuche es erneut!")

    eingabe = False

# Berechnung der Note anhand der Auswahl

if (auge == 1) and (frisur == 1): 
    note = note * 1.1
if (auge == 1) and (frisur == 0): 
    note = note * 0.9
if (auge == 0) and (frisur == 1): 
    note = note * 1.1
if (auge == 0) and (frisur == 0): 
    note = note * 0.9
if wetter == 1:
    note = note - 1

# Ausgabe der Note
print(f"Die Note der Schüler:in beläuft sich durch die gegebenen Bedingungen auf {round(note, 2)}.")