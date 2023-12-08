class Vorlesung:
    def __init__(self):
        self.titel = ""
        self.studierende = []
        self.zoomlink = "default"
    
    def schreibeEin(self, name):
        self.studierende.append(name)
    
    def schreibeAus(self, name):
        for i, elem in enumerate(self.studierende):
            if elem == name:
                self.studierende.pop(i)

    def getStudierende(self):
        self.studierende.sort()
        print(self.studierende)
    
    def getAnzahlStudierende(self):
        anzahl = 0
        for i in self.studierende:
            anzahl += 1
        print(anzahl)

        

mathe = Vorlesung()
mathe.schreibeEin("Torge")
mathe.schreibeEin("Ove")
mathe.schreibeEin("Tilo")
mathe.getStudierende()
mathe.getAnzahlStudierende()