import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd

# Daten einlesen
data = pd.read_csv("code_examples\\NAHSH_Verkehr\\ein_aussteiger.csv", delimiter=";")

# Suchen und Anzeigen der Haltestelle
def search_haltestelle():
    search_text = search_entry.get()
    result = data[data['haltestelle'].str.contains(search_text, case=False)]
    haltestellen = result['haltestelle'].unique()

    haltestelle_menu['values'] = tuple(haltestellen)
    haltestelle_menu.set(haltestellen[0])

    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result.to_string(index=False))
    result_text.config(state="disabled")

# Erstellen des Graphen
def create_graph():
    haltestelle = selected_haltestelle.get()
    selected_day = selected_day_var.get()
    haltestelle_data = data[(data['haltestelle'] == haltestelle) & (data['tage'] == selected_day)]
    years = haltestelle_data['jahr']
    einsteiger = haltestelle_data['durchschnitt_einsteiger_tag'].str.replace('.', '').str.replace(',', '.').astype(float)
    aussteiger = haltestelle_data['durchschnitt_aussteiger_tag'].str.replace('.', '').str.replace(',', '.').astype(float)

    plt.figure(figsize=(10, 6))
    plt.plot(years, einsteiger, label='Durchschnitt Einsteiger')
    plt.plot(years, aussteiger, label='Durchschnitt Aussteiger')
    plt.xlabel('Jahr')
    plt.ylabel('Durchschnittliche Ein- und Aussteiger')
    plt.title(f'Durchschnittliche Ein- und Aussteiger für {haltestelle} ({selected_day})')
    plt.legend()
    plt.grid(True)
    plt.show()

# GUI erstellen
app = tk.Tk()
app.title("Haltestellensuche und Graph")

search_label = ttk.Label(app, text="Suche nach Haltestelle:")
search_label.pack(padx=10, pady=5)

search_entry = ttk.Entry(app)
search_entry.pack(padx=10, pady=5)

search_button = ttk.Button(app, text="Suchen", command=search_haltestelle)
search_button.pack(padx=10, pady=5)

result_text = tk.Text(app, height=10, width=40)
result_text.config(state="disabled")
result_text.pack(padx=10, pady=5)

selected_haltestelle = tk.StringVar()
selected_haltestelle.set(data['haltestelle'].values[0])

haltestelle_label = ttk.Label(app, text="Wähle eine Haltestelle:")
haltestelle_label.pack(padx=10, pady=5)

haltestelle_menu = ttk.Combobox(app, textvariable=selected_haltestelle, values=data['haltestelle'].unique())
haltestelle_menu.pack(padx=10, pady=5)

selected_day_var = tk.StringVar()
selected_day_var.set("Mo-Fr")  # Default selection

day_label = ttk.Label(app, text="Wähle einen Tag:")
day_label.pack(padx=10, pady=5)

day_menu = ttk.Combobox(app, textvariable=selected_day_var, values=["Mo-Fr", "Mo-So", "Sa", "So"])
day_menu.pack(padx=10, pady=5)

create_graph_button = ttk.Button(app, text="Graph erstellen", command=create_graph)
create_graph_button.pack(padx=10, pady=5)

app.mainloop()
