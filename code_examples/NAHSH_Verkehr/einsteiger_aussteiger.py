import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd

# Daten einlesen
data = pd.read_csv("code_examples\\NAHSH_Verkehr\\ein_aussteiger.csv", delimiter=";")

# Suchen und Anzeigen der Haltestelle
def suche_haltestelle():
    suchtext = eingabe_haltestelle.get()
    ergebnis = data[data['haltestelle'].str.contains(suchtext, case=False)]
    haltestellen = ergebnis['haltestelle'].unique()

    auswahl_haltestelle['values'] = tuple(haltestellen)
    auswahl_haltestelle.set(haltestellen[0])

    ausgabe_text.config(state="normal")
    ausgabe_text.delete(1.0, tk.END)
    ausgabe_text.insert(tk.END, ergebnis.to_string(index=False))
    ausgabe_text.config(state="disabled")

# Erstellen des Graphen
def erstelle_graph():
    haltestelle = auswahl_haltestelle.get()
    ausgewaehlter_tag = ausgewaehlter_tag_var.get()
    haltestelle_data = data[(data['haltestelle'] == haltestelle) & (data['tage'] == ausgewaehlter_tag)]
    jahre = haltestelle_data['jahr']
    einsteiger = haltestelle_data['durchschnitt_einsteiger_tag'].str.replace('.', '').str.replace(',', '.').astype(float)
    aussteiger = haltestelle_data['durchschnitt_aussteiger_tag'].str.replace('.', '').str.replace(',', '.').astype(float)

    plt.figure(figsize=(10, 6))
    plt.plot(jahre, einsteiger, label='Durchschnitt Einsteiger')
    plt.plot(jahre, aussteiger, label='Durchschnitt Aussteiger')
    plt.xlabel('Jahr')
    plt.ylabel('Durchschnittliche Ein- und Aussteiger')
    plt.title(f'Durchschnittliche Ein- und Aussteiger für {haltestelle} ({ausgewaehlter_tag})')
    plt.legend()
    plt.grid(True)
    plt.show()

# GUI erstellen
app = tk.Tk()
app.title("Haltestellensuche und Graph")

such_label = ttk.Label(app, text="Suche nach Haltestelle:")
such_label.pack(padx=10, pady=5)

eingabe_haltestelle = ttk.Entry(app)
eingabe_haltestelle.pack(padx=10, pady=5)

suchen_button = ttk.Button(app, text="Suchen", command=suche_haltestelle)
suchen_button.pack(padx=10, pady=5)

ausgabe_text = tk.Text(app, height=10, width=40)
ausgabe_text.config(state="disabled")
ausgabe_text.pack(padx=10, pady=5)

auswahl_haltestelle = ttk.Combobox(app, textvariable=selected_haltestelle, values=data['haltestelle'].unique())
auswahl_haltestelle.pack(padx=10, pady=5)

ausgewaehlter_tag_var = tk.StringVar()
ausgewaehlter_tag_var.set("Mo-Fr")  # Standardauswahl

tag_label = ttk.Label(app, text="Wähle einen Tag:")
tag_label.pack(padx=10, pady=5)

tag_auswahl = ttk.Combobox(app, textvariable=ausgewaehlter_tag_var, values=["Mo-Fr", "Mo-So", "Sa", "So"])
tag_auswahl.pack(padx=10, pady=5)

graph_erstellen_button = ttk.Button(app, text="Graph erstellen", command=erstelle_graph)
graph_erstellen_button.pack(padx=10, pady=5)

app.mainloop()
