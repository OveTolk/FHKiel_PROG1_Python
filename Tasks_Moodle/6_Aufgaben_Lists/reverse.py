# Python Reverse 

def reverseText(text):
    text = text
    reverse = []
    reverseTextResult = ""
    for elem in text:
        reverse.insert(0, elem)
    for elem in reverse:
        reverseTextResult = reverseTextResult + elem
    return reverseTextResult

def main():
    text = input("Geben Sie einen Text ein, der reversed werden soll: ")
    print(reverseText(text))    

main()