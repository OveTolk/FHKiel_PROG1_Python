class Room:
    def __init__(self, nummer):
        self.list = {}
        self.list[nummer] = True
        print(self.list)

class Hotel():     
    def isAvailable(self, nummer):
        if Room.list[nummer] == True:
            return True
        elif Room.list[nummer] == False:
            return False
        else:
            print("Fehler in der isAvailable()")

    def setAvailable(self, nummer):
        if self.list[nummer] == True:
            self.list[nummer] == False
        elif self.list[nummer] == False:
            self.list[nummer] == True
        else: 
            print("Fehler in der setAvailable()")

rooms = []
rooms.append(Room(101))
rooms.append(Room(102))
rooms.append(Room(103))
rooms.append(Room(201))
rooms.append(Room(202))
rooms.append(Room(203))

hotel = Hotel()
hotel.isAvailable(203)