import mysql.connector
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Verbindung zur MySQL-Datenbank herstellen
db = mysql.connector.connect(
    host="192.168.98.238",
    user="python",
    passwd="SQL2023!",
    database="polizei"
)

# Ein Cursor-Objekt erstellen, um SQL-Abfragen auszuführen
cursor = db.cursor()

# SQL-Abfrage, um die Latitude und Longitude abzurufen
query = "SELECT latitude, longitude FROM dienststellen"
cursor.execute(query)

# Alle abgerufenen Datensätze holen
locations = cursor.fetchall()

# Karte erstellen
plt.figure(figsize=(12, 9))
m = Basemap(projection='mill',llcrnrlat=53,urcrnrlat=55,llcrnrlon=7,urcrnrlon=12,resolution='c')
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.drawcoastlines()
m.drawparallels(range(-90, 91, 30), labels=[1,0,0,0])
m.drawmeridians(range(-180, 181, 60), labels=[0,0,0,1])

# Marker für jede Position hinzufügen
for location in locations:
    latitude_str, longitude_str = location[0], location[1]
    
    try:
        lat, lon = float(latitude_str), float(longitude_str)
        x, y = m(lon, lat)
        m.plot(x, y, 'bo', markersize=8)
    except ValueError as e:
        print(f"Fehler beim Konvertieren der Werte: {e}")
        print(f"Problematische Werte: Latitude: {latitude_str}, Longitude: {longitude_str}")

# Karte anzeigen
plt.title('Dienststellen Karte')
plt.show()

# Verbindung schließen
db.close()
