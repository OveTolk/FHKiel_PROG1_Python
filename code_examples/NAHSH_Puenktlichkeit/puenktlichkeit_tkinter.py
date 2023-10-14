# Dieser Code visualisiert die Pünktlichkeit des NAH_SH von 2010 bis 2022

import matplotlib.pyplot as plt
from tkinter import *
import pandas as pd

# CSV-Datei importieren
file_path = "code_examples\\NAHSH_Puenktlichkeit\\puenktlichkeit.csv"

# Tkinter Fesnter
root = Tk()
root.title("Pünktlichkeit")
line_listbox = Listbox(root)
line_listbox.pack()
# Daten in Data Frame 
df = pd.read_csv(file_path, delimiter=";")

# Linien in die Listbox einfügen
for line in df["linie"].unique():
    line_listbox.insert(END, line)

# Funktion zum Erstellen des Graphen
def create_graph():
    selected_line = line_listbox.get(ACTIVE)
    df_line = df[df["linie"] == selected_line]

    # Konvertiere in Datetime für bessere Darstellung
    df_line["Date"] = pd.to_datetime(df_line["jahr"].astype(str) + df_line["monat"].astype(str), format="%Y%m")
    
    # Konvertiere in Dezimalwert für bessere Darstellung
    df_line["puenktlichkeitsniveau_an"] = df_line["puenktlichkeitsniveau_an"].str.replace(',', '.').astype(float)

    # Plot erstellen
    plt.figure(figsize=(10, 6))
    plt.plot(df_line["Date"], df_line["puenktlichkeitsniveau_an"])
    plt.ylabel("Pünktlichkeit")
    plt.xlabel("Jahr-Monat")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Button erstellen
button = Button(root, text="Graph erstellen", command=create_graph)
button.pack()

# Programm starten
root.mainloop()
