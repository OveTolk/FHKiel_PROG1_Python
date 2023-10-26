# Dieses Programm berechnet den Anhalteweg bei einer bestimmten Geschwindigkeit.

# Eingabe der Geschwindigkeit
def inputUser():
    geschwindigkeit = input("Geben Sie die Geschwindigkeit des Autos ein: ")
    return float(geschwindigkeit)

# Berechnung des Reaktionswegs
def reaktionsweg(kmh):
    rweg = (kmh/10)*3
    return rweg

# Berechnung des Bremswegs
def bremsweg(kmh):
    bweg = (kmh/10)*(kmh/10)
    return bweg

# Berechnungs des Anhaltewegs
def anhalteweg(rweg, bweg):
    aweg = rweg+bweg
    return aweg

# Ausgabe der Berechnungen
def output(kmh, rweg, bweg, aweg):#
    print(f"Bei einer Geschwindigkeit von {kmh} berechnen sich folgende Wege:")
    print(f"Reaktionsweg    : {rweg} m")
    print(f"Bremsweg        : {bweg} m")
    print(f"Anhalteweg      : {aweg} m")

# Haupt Programm
def main():
    print("Dieses Programm berechnet den Reaktionsweg, Bremsweg und Anhalteweg anhand einer eingegeben Geschwindigkeit.")
    kmh = inputUser()
    rweg = reaktionsweg(kmh)
    bweg = bremsweg(kmh)
    aweg = anhalteweg(rweg, bweg)
    output(kmh, rweg, bweg, aweg)

main()