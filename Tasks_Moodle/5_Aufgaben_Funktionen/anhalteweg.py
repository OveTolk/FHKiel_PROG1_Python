def inputUser():
    geschwindigkeit = input("Geben Sie die Geschwindigkeit des Autos ein: ")
    return float(geschwindigkeit)

def reaktionsweg(kmh):
    rweg = (kmh/10)*3
    return rweg

def bremsweg(kmh):
    bweg = (kmh/10)*(kmh/10)
    return bweg

def anhalteweg(rweg, bweg):
    aweg = rweg+bweg
    return aweg

def main():
    kmh = inputUser()
    rweg = reaktionsweg(kmh)
    bweg = bremsweg(kmh)
    aweg = anhalteweg(rweg, bweg)
    print(aweg)

main()