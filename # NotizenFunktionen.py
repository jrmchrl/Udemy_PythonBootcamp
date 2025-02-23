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

print(len("Hallo"))

print(len(["Hallo", "Welt"]))

# Mehrere Parameter übergeben

def multi_print(name, count):
    for i in range(0, count):
        print(name)

multi_print("Hallo!", 5)

# Selbst definierte Funktion innerhalber einer weiteren aufrufen

def weitere_funktion():
    multi_print("Hallo!", 3)
    multi_print("Welt!", 3)

weitere_funktion()

# Funktion die Ergebnis zurückgibt, mit dem ich weiterarbeiten kann

def maximum(a, b):
    if a < b:
        return b
    else:
        return a

result = maximum(4, 5)

print(result)

# Es gibt Variablen, die intern eingebaut Funktionen enthalten - es gibt normale Funktionen und Funktionen, die wir auf einem "Objekt" ausführen können

liste = [1,2,3]

print(liste)

liste.append(4) #Funktion append hat Besonderheit, dass vor ihr etwas steht, in diesem Fall liste, Liste ist damit Variable, in der List steht uns die Funktion append zur Verfügung

print(liste)

# .split gehört auch dazu

# Arbeiten mit Dateien

# lesen & schreiben

# CSV einlesen


