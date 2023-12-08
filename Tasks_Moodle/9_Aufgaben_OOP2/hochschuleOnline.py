import hochschule

class VorlesungOnline(hochschule.Vorlesung):
    def setZoom(self, link):
        self.zoomlink = link
    
    def getZoom(self):
        print(self.zoomlink)

test = VorlesungOnline()
test.setZoom("zoom.com")
test.getZoom()