# User-Input des Bruttobetrags
brutto = float(input("Geben Sie den Bruttobetrag ein: "))

# Höhe des Steuersatzes
mwst_satz = 0.19

# Berechnung der Höhe der Steuer
mwst = brutto * mwst_satz

# Berechnung des Nettobetrags
netto = brutto - mwst

# Ausgabe aller drei Variablen
print(f"Der Bruttobetrag beträgt {brutto} €. Die Höhe der MWST liegt bei {round(mwst, 2)} €. Daher ist der Nettobetrag {netto} €")