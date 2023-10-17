# Quelle: https://opendata.schleswig-holstein.de/dataset/passagiere-schiffsverkehr-der-kieler-schlepp-und-fahrgesellschaft

import matplotlib.pyplot as plt
import pandas as pd

pfad = "code_examples\\Kieler_Faehre\\stats.csv"

stats = pd.read_csv(pfad, delimiter=";")

x = stats["Jahr"]
y = stats["Fahrgaeste"].astype(int)

plt.plot(x, y)
plt.show()
