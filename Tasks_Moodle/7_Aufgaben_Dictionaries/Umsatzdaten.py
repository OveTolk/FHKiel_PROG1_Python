umsatz = [100, 200, None, 300, None, 400]

for i, enum in enumerate(umsatz):
    avg = 0
    if enum == None:
        avg = (umsatz[i-1] + umsatz[i+1]) / 2
        umsatz.pop(i)
        umsatz.insert(i, avg)

print(umsatz)