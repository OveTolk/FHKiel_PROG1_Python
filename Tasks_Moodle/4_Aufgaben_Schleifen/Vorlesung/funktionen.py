def schoen(text, verzierung):
    data = f"{verzierung} {text} {verzierung}"
    return data
def ausgabe(name, verzierung):
    print(schoen(name, verzierung))

name = input("Name: ")
verzierung = input("Verzierung: ")

ausgabe(name, verzierung)