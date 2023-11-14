# WWWWWWBBSSSSS zu 5W2B5S komprimieren

def komprimieren(string):
    list = []
    i = 0 
    for i, letter in enumerate(string):
        if letter == string[i+1]:
            list.append(f"{i+1}{letter}")
        else:
            pass
    
    print(list)
            


def main():
    string = input("Geben Sie den String an, der komprimiert werden soll: ")
    komp = komprimieren(string)
main()