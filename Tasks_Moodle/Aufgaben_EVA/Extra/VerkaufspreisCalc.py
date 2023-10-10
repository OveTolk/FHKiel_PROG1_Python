# Dieses Programm bestimmt den Verkaufspreis eines Produktes mit einer bestimmten Marge.

fix = float(input("Geben Sie die Kosten des Produkts an (€) an: "))
marge = float(input("Geben Sie die gewünschte Marge (%) an: "))

verkaufspreis = fix + (fix * (marge / 100))
print(f"Der Verkauspreis muss bei {verkaufspreis} € liegen um eine Marge von {marge} % zu erreichen.")