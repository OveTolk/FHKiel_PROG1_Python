class Warteschlange:
    def __init__(self):
        self.warteschlange = []
    def ausgabe(self):
        print(self.warteschlange)
    def ankommen(self, name):
        nameex = name
        self.warteschlange.append(nameex)
    def verlassen(self):
        self.warteschlange.pop(0)

w = Warteschlange()
w.ausgabe()
w.ankommen("Alina")
w.ausgabe()
w.ankommen("Bernd")
w.ausgabe()
w.ankommen("Christoph")
w.ausgabe()
w.verlassen()
w.ausgabe()
w.verlassen()
w.ausgabe()
w.verlassen()
w.ausgabe()