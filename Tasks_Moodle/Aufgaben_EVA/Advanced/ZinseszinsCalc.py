import matplotlib.pyplot as plt
import numpy as np

# Erklärung was das Programm macht
print("Dieses Programm errechnet den Zinseszins eines Anfangskapitals mit einem konstanten Zins und einer bestimmten Laufzeit.")

# Bestimmung der benötigten Eingaben
anfangskapital = float(input("Geben Sie das Anfangskapital (€) ein: "))
zinssatz = float(input("Geben Sie den Zinssatz (%) ein: "))
laufzeit = int(input("Geben Sie die Laufzeit (in Jahren): "))

x = []
y = []

jahr = 0
while jahr < laufzeit + 1:
    endkapital = anfangskapital * (1 + zinssatz / 100) ** jahr
    x.append(jahr)
    y.append(endkapital)
    jahr += 1

x_values = np.array(x)
y_values = np.array(y)

plt.plot(x_values, y_values)
plt.show()
