class Kaffeemaschine:
    def __init__(self):
        self.kaffeesorten = {
            "Crema": 0,
            "Cappuccino": 0,
            "Kakao": 0,
            "Espresso": 0,
            "Americano": 0,
            "Latte Macchiato": 0,
            "Flat White": 0
        }
    def zubereiten(self, auswahl):
        if auswahl in self.kaffeesorten:
            self.kaffeesorten[auswahl] = self.kaffeesorten[auswahl] + 1
            print(f"Die Auswahl: {auswahl} wird zubereitet!")
        else: 
            print(f"Die Kaffeesorte ist nicht verfügbar.")

    def anzeige(self):
        for auswahl in self.kaffeesorten:
            print(f"{auswahl}: {self.kaffeesorten[auswahl]}")
    
    


    
jura1 = Kaffeemaschine()
jura1.zubereiten("Americano")
jura1.anzeige()