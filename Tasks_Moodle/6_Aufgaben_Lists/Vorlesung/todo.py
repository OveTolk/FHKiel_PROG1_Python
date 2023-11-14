aufgaben = ["Vorlesung", "Python lernen", "Einkaufen"]

test = len(aufgaben)
print(test)
for i, elem in enumerate(aufgaben):
    print(f"Als {i+1}. mache ich {elem}")

if aufgaben[0:1] == "Vorlesung":
    print("Schade")
else:
    print("Nein")