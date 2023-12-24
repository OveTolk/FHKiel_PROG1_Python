import csv
import mysql.connector

# Verbindung zur MySQL-Datenbank herstellen
db = mysql.connector.connect(
    host="192.168.98.238",
    user="python",
    passwd="SQL2023!",
    database="polizei"
)

# Ein Cursor-Objekt erstellen, um SQL-Abfragen auszuführen
cursor = db.cursor()

# CSV-Datei öffnen und Daten lesen
with open('C:/Users/Ove Tolk/Downloads/polizeidienststellen.csv', 'r', encoding='utf-8') as csvfile:
    csv_data = csv.reader(csvfile, delimiter='\t')  # Tabulator als Trennzeichen verwenden
    
    # Durch die CSV-Datei iterieren und Daten in die Datenbank einfügen
    for row in csv_data:
        # Überprüfen, ob die Zeile nicht leer ist
        if row:
            # Anzahl der erwarteten Werte überprüfen
            if len(row) == 13:
                id, name, city, zipcode, street, houseNumber, telephone, fax, email, website, longitude, latitude, _ = row
                cursor.execute("INSERT INTO dienststellen (id, name, city, zipcode, street, houseNumber, telephone, fax, mail, website, longitude, latitude) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (id, name, city, zipcode, street, houseNumber, telephone, fax, email, website, longitude, latitude))
            else:
                print(f"Ungültige Zeile: {row}. Erwartet wurden 13 Werte.")
        else:
            print("Leere Zeile übersprungen.")

# Änderungen in der Datenbank bestätigen
db.commit()

# Verbindung schließen
db.close()
