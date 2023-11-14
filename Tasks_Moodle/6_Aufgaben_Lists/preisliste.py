# Gegeben sei folgende Preisliste von Produkten:
produktpreise = [100, 150, 200, 250, 300, 500, 20, 30, 80, 12, 8, 23, 45]

# Berechnen Sie den Durchschnittspreis mit einer For-Schleife und geben Sie das Ergebnis aus.
avg = 0
for i, elem in enumerate(produktpreise):
    avg+=elem

leng = len(produktpreise)
ergebnis = avg/leng

print(f"Der Durchschnittspreis beträgt: {round(ergebnis, 2)} Euro.")