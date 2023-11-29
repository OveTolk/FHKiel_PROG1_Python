class Senderauswahl:
    def __init__(self):
        self.kanaldict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25, 26:26, 27:27, 28:28, 29:29, 30:30}
        self.currentkanal = 1
    def changeSender(self, kanal):
        self.currentkanal = kanal
    def changeSenderName(self, name):
        self.kanaldict[self.currentkanal] = name
    def output(self):
        return self.kanaldict

def outputSenderliste():
    fernseher = Senderauswahl()
    dict = fernseher.output()
    for i in dict:
        print(f"Kanal: {i} | Name: {dict[i]}")

def renewSender():
    fernseher = Senderauswahl()
    name = input("Geben Sie den gewünschten Namen ein: ")
    fernseher.changeSenderName(name)

def changeCurrentSender():
    fernseher = Senderauswahl()
    kanal = input("Zu welchem Kanal möchten Sie wechseln: ")
    fernseher.changeSender(kanal)
    print(f"Sie sind auf dem Kanal: {fernseher.currentkanal}")

def menu():
    print("1: Senderliste ausgeben")
    print("2: Sendername aktualisieren")
    print("3: Aktuellen Sender auswählen")
    print("4: Fernseher ausschalten")
    auswahl = int(input("Wählen Sie eine Option aus: "))
    if auswahl == 1:
        outputSenderliste()
    elif auswahl == 2:
        renewSender()
    elif auswahl == 3:
        changeCurrentSender()
    elif auswahl == 4:
        main(False)
    else:
        print("Geben Sie eine Zahl von 1 und 4 ein.")
def main(statein):
    state = statein
    print(state)
    while state == True:
        menu()

main(True)