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
    }
    converted = json.dumps(all_entries, indent=4)
    print(converted)
    requests.get("http://localhost:3007/creategraph", data=converted)

tk.Button(text="Create graph", command=load).grid(row=9)

tk.mainloop()
