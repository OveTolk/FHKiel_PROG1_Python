import matplotlib.pyplot as plt

# User Input für Variablen
fix = float(input("Bitte geben Sie die Fixkosten ein: "))
variabel = float(input("Bitte geben Sie die variablen Kosten (pro Produkt) ein: "))
preis = float(input("Bitte geben Sie den Verkaufspreis pro Produkt ein: "))

# Berechnung des Break-Even-Points
breakeven = fix / (preis - variabel)
start = 1
start2 = 1
end = breakeven * 2

umsatz_x = []
umsatz_y = []
kosten_x = []
kosten_y = []

while start < end + 1:
    umsatz = preis * start
    umsatz_x.append(start)
    umsatz_y.append(umsatz)
    start += 1

while start2 < end + 1:
    kosten = fix + (variabel * start2)
    kosten_x.append(start2)
    kosten_y.append(kosten)
    start2 += 1

plt.suptitle("Break-Even-Analyse")
plt.title(f"Der Break-Even-Punkt ist bei {round(breakeven, 2)} Einheiten.")
plt.plot(umsatz_x, umsatz_y, label = "Umsatz")
plt.plot(kosten_x, kosten_y, label = "Kosten")
plt.xlabel("Menge")
plt.ylabel("Kosten")
plt.legend()
plt.show()