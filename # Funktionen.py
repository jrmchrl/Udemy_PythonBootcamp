# Funktionen
# Erhalten Übersicht, logische Blöcke entwickeln, übersichtliches Programm

print("Hallo Welt")  # Funktion, die Funktionsparameter aufruft

def multi_print(): # def -- das ist der Name der Funktion - "Definiere ein Rezept, Rezept kann dann ausgegeben werden"
    print("Hallo Welt")
    print("Hallo Welt")

multi_print()  # Funktion MUSS dann aber noch ausgegeben werden -- Rezept gekocht werden  

# Funktion kann Parameter übergeben werden

def multi_print2(name): #hier wird Variable übergeben
    print(name)
    print(name)

multi_print2("Schnute")