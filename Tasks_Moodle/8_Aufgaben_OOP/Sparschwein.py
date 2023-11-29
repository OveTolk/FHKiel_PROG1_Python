class Sparschwein:
    def __init__(self):
        self.geldbetrag = 0
    def einzahlen(self, geld):
        self.geldbetrag += geld
        print(f"{geld} erfolgreich eingezahlt.")
    def abheben(self, geld):
        self.geldbetrag -= geld
        print(f"{geld} erfolgreich ausgezahlt.")
    def zeige_geldbestand(self):
        print(f"Dein Geldbestand beträgt {self.geldbetrag} Euro")

rosa_sparschwein = Sparschwein()
rosa_sparschwein.einzahlen(120)
rosa_sparschwein.abheben(90)
rosa_sparschwein.abheben(50)
rosa_sparschwein.zeige_geldbestand()
