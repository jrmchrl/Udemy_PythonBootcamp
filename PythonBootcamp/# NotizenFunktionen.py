# Funktionen
# Erhalten Übersicht, logische Blöcke entwickeln, übersichtliches Programm

print("Hallo Welt")  # Funktion, die Funktionsparameter aufruft

def multi_print(): # def -- das ist der Name der Funktion - "Definiere ein Rezept, Rezept kann dann ausgegeben werden"
    print("Hallo Welt")
    print("Hallo Welt")

multi_print()  # Funktion MUSS dann aber noch ausgegeben werden -- Rezept gekocht werden  

# Funktion kann Parameter übergeben werden
my_list = [4,5,8,1]
doppelt = my_list * 2

print(doppelt)

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


file = open("Hallo du,", "r")
for line in file:
    print(line)
    print("Wurmtext der Zeilen trennt")

# \n  --> geht in neue Zeile - steht ebenfalls in jeder Zeile der Textdatei, nur, dass man es nicht sieht

file = open("Hallo du,", "r")
for line in file:
    print(line.strip()) #entfernt Steuer- und Leerzeichen weg


# Datei beschreiben
    
file = open("schreiben.txt", "w") #"a" bedeutet append, hänge Elemente einfach nur am Ende dazu

students =["Nadina", "Dunja", "Mona", "Clara"]

for student in students:
    file.write(student + "\n")

file.write("So einfach kannst du eine Datei erstellen \n& reinschreiben")

file.close()

# Datei und with

#file.close() ist nicht so robust, denn sobald Fehler in Zeile davor erfolgt, wird file.close() gar nicht erreicht
# mit with und as file, wird Datei in jedem Fall wieder geschlossen
with open("Hallo du,", "r") as file:
    for line in file:
        print(line)

# CSV öffnen


with open ("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
        print(data[0] + ": " + data[1])


print("Muenchen;1800000;MUC".split(";"))

# CSV lesen und Daten überspringen

with open("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
        if data[0] == "Muenchen" or data[0] == "Budapest":
            print(data[0])
            print(data)

# Nach Zahl filtern
            
with open("datei.csv") as file:
    for line in file:
        data = line.strip().split(";")   
        if int(data[1]) >= 2000000:
            print(data)    


