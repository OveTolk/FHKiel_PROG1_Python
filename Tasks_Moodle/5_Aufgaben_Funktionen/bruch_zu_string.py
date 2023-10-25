# Funktion erstellen, die einen Zähler und Nenner darstellt

def bruch_zu_string(a, b):
        print(f"{a}" + "/" + f"{b}")

a = input("Geben Sie den Zähler ein: ")
b = input("Geben Sie den Nenner ein: ")
bruch_zu_string(a, b)