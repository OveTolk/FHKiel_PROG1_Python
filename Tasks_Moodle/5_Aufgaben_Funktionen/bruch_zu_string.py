# Funktion erstellen, die einen Zähler und Nenner darstellt
def bruch_zu_string(a):
        text1, text2 = a
        print(f"{text1}" + "/" + f"{text2}")

# Eingabe des Benutzers
def inputUser():
    a = input("Geben Sie den Zähler ein: ")
    b = input("Geben Sie den Nenner ein: ")
    return(a,b)

# Haupt Funktion
def main():
    print("Dieses Programm erstellt mit den Eingaben des Users einen Bruch und gibt diesen aus.")
    vars = inputUser()
    bruch_zu_string(vars)

main()