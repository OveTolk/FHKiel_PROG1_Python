import tkinter as tk
import json
import requests

root = tk.Tk()
root.wm_title("Project Summary")
tk.Label(text="Initiative name:").grid(row=0)
tk.Label(text="Initiative goals:").grid(row=1)
tk.Label(text="Project leader:").grid(row=2)
tk.Label(text="Sponsor:").grid(row=3)
tk.Label(text="Status:").grid(row=4)
tk.Label(text="Expected benefits:").grid(row=5)  # Corrected typo
tk.Label(text="Required investments:").grid(row=6)
tk.Label(text="Risks:").grid(row=7)
tk.Label(text="Dependencies:").grid(row=8)

entry0 = tk.Entry()
entry1 = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()
entry4 = tk.Entry()
entry5 = tk.Entry()
entry6 = tk.Entry()
entry7 = tk.Entry()
entry8 = tk.Entry()
entry9 = tk.Entry()

entry0.grid(row=0, column=1)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
entry3.grid(row=3, column=1)
entry4.grid(row=4, column=1)
entry5.grid(row=5, column=1)
entry6.grid(row=6, column=1)
entry7.grid(row=7, column=1)
entry8.grid(row=8, column=1)

timeline_entries = []

def add_timeline_entry():
    date = date_entry.get()
    event = event_entry.get()
    description = description_entry.get()
    color = color_entry.get()
    
    if date and event and description and color:
        entry = {
            "date": date,
            "event": event,
            "description": description,
            "color": color
        }
        timeline_entries.append(entry)
        clear_timeline_fields()
        update_timeline_display()

def clear_timeline_fields():
    date_entry.delete(0, "end")
    event_entry.delete(0, "end")
    description_entry.delete(0, "end")
    color_entry.delete(0, "end")

def update_timeline_display():
    timeline_display.config(state="normal")
    timeline_display.delete("1.0", "end")
    for entry in timeline_entries:
        timeline_display.insert("end", json.dumps(entry, indent=4) + "\n")
    timeline_display.config(state="disabled")

# Labels und Entry-Felder für Timeline-Einträge
tk.Label(text="Date:").grid(row=9, column=0)
tk.Label(text="Event:").grid(row=10, column=0)
tk.Label(text="Description:").grid(row=11, column=0)
tk.Label(text="Color:").grid(row=12, column=0)

date_entry = tk.Entry()
event_entry = tk.Entry()
description_entry = tk.Entry()
color_entry = tk.Entry()

date_entry.grid(row=9, column=1)
event_entry.grid(row=10, column=1)
description_entry.grid(row=11, column=1)
color_entry.grid(row=12, column=1)

# Button zum Hinzufügen von Timeline-Einträgen
add_timeline_button = tk.Button(text="Add Timeline Entry", command=add_timeline_entry)
add_timeline_button.grid(row=13, column=0)

# Ein Textfeld zur Anzeige der Timeline-Einträge
timeline_display = tk.Text(height=5, width=40, state="disabled")
timeline_display.grid(row=14, column=1)

def load():
    all_entries = {
        "Initiative name": entry0.get(),
        "Initiative goals": entry1.get(),
        "Project leader": entry2.get(),
        "Sponsor": entry3.get(),
        "Status": entry4.get(),
        "Expected benefits": entry5.get(),
        "Required investments": entry6.get(),
        "Risks": entry7.get(),
        "Dependencies": entry8.get(),
        "Datapoints": timeline_entries
    }
    converted = json.dumps(all_entries, indent=4)
    # print(converted)
    headers = {'Content-type': 'application/json'}
    requests.get("http://ts.ovetolk.eu:3007/creategraph", data=converted, headers=headers)

tk.Button(text="Create graph", command=load).grid(row=15)

tk.mainloop()
