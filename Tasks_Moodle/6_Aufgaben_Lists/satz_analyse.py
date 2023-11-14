# Dieses Programm berechnet die Anzahl an Wörter im Satz und analysiert die durchschnittliche Wortlänge

def countWords(satz):
    satz = satz.split(" ")
    return len(satz)

def countWordLen(satz):
    satz = satz.split(" ")
    elems = len(satz)
    wordLengths = []
    for elem in satz:
        for i in elem:
            laenge = len(i)
            wordLengths.append(laenge)
    
    summeWordLength = 0
    for elem in wordLengths:
        summeWordLength = summeWordLength + elem
    avg = summeWordLength/elems
    return avg
        
def main():
    satz = input("Geben Sie einen Satz ein, der analysiert werden soll: ")
    lenSatz = countWords(satz)
    lenWord = countWordLen(satz)
    print(f"Anzahl der Wörter im Satz: {lenSatz}")
    print(f"Durchschnittliche Wortlänge: {round(lenWord, 2)} Zeichen")

main()