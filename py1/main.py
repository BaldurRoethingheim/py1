'''
This is a 
multi line 
comment.
'''
# this is a single line comment

b_exec_all = False
false = False  # False bool
true = True    # True bool
str_trennlinie = "\r\n\r\n----------------------------------------------------------------------------"

# tutorial "https://www.youtube.com/watch?v=oxXAb8IikHM&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB"

# ex_1 Dein erstes Programm
import numbers
from os import name
from string import printable
from tkinter import SEL
from typing import Counter

if (b_exec_all):
        
    print(str_trennlinie)
    print("'# ex_1 Dein erstes Programm'"
    "\r\n")
        
    print("Hey.\r\n"
          "How are you?")
    def print_hi(name):
        print(f'Hallo, {name}.')    
    if __name__ == '__main__':
        print_hi('Welt')    
    print("Hallo Welt, ich lerne gerade programmieren.")

# ex_2 Zahlen in Python
if (b_exec_all):
       
    print(str_trennlinie)
    print("'# ex_2 Zahlen in Python'"
    "\r\n")
    
    print(-7)
    print(8/4)
    print((3+2)*(2-1))
    print(2.1 + 1.5)
    print(2.4*2)

# ex_3 Strings in Python
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_3 Strings in Python'"
    "\r\n")
    
    print("Hallo Welt")
    print('Hallo '+'Welt.')
    # mehrzeiliger String
    print('''Die 
    Programmiersprache "Python" ist cool.''')
    print("""Die 
    Programmiersprache "Python" ist cool.""")

# ex_4 Variablen
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_4 Variablen'"
    "\r\n")
    num_age = 27
    str_name = "Markus"
    print(num_age)
    num_age = 28
    print(num_age)
    print(str_name)

# ex_5 Datentypen int, float, str
if (b_exec_all):
    
    print(str_trennlinie)
    print("'# ex_5 Datentypen int, float, str'"
    "\r\n")
    
    print("String " + "Verkettung")
    print(10+3)
    # print(10+"String") # Fehler
    int_variable_zahl = 100
    float_variable = 13.734
    str_variable1 = "Das ist ein String."
    str_variable2 = 'Das ist ein String.'

# ex_6 Die input()-Funktion
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_6 Die input()-Funktion'"
    "\r\n")
    
    print("Angfang des Programms")
    str_name = input("Hinweis: Bitte deinen Namen eingeben:")
    print("Meine Name ist " + str_name)
    num_age = input("Hinweis: Bitte dein Alter eingeben:")
    print("Mein Alter ist " + num_age)
    print("Ende des Programms")

# ex_7 Type-Casting-Funktionen
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_7 Type-Casting-Funktionen'"
    "\r\n")
    
    value1 = input("Erste Zahle eingeben: ")
    value2 = input("Zweite Zahle eingeben: ")
    
    type_of_value = type(value1)
    print(type_of_value)
    print(value1)
    type_of_value = type(value2)
    print(type_of_value)
    print(value2)
    
    print(value1+value2)
    print(int(value1) + int(value2))
    
    value1 = int(value1)
    value2 = int(value2)
    print((value1+value2))
    
    print(int(value1+value2))
    print(float(value1+value2))
    print(str(value1+value2))

# ex_8 Der Zuweisungsoperator
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_8 Der Zuweisungsoperator'"
    "\r\n")
    
    example1 = 22
    
    example2 = 22 + 3
    
    example3 = (22 - 2) * 3
    
    value1 = 5
    value2 = 5
    
    value1 = value1 + 10
    print(value1)
    
    value2 /= 2
    print(value2)

# ex_9 Vergleichsoperatoren und der Datentyp bool
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_9 Vergleichsoperatoren und der Datentyp bool'"
    "\r\n")
    
    print(1 < 5) # (<) kleiner als Operator
    print(5 < 1)
    print(1 > 5) # (>) größer als Operator
    print(5 > 1)
    
    print(type(1 < 5))
    print(type(5 < 1))
    print(type(1 > 5))
    print(type(5 > 1))
    
    print(1 <= 5) # (<=) kleiner als oder gleich Operator
    print(5 <= 5)
    print(6 <= 5)
    print(1 >= 5) # (<=) größer als oder gleich Operator
    print(5 >= 5)
    print(6 >= 5)
    
    print(4 != 5) # (!=) ungleich Operator
    print((4 + 2) * 3 == 5) # (==) gleich Operator    

# ex_10 Die if Anweisung
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_10 Die if Anweisung'"
    "\r\n")
    
    age = int(input("Bitte gebe dein Alter ein: "))
    
    if age  < 18:
        print("Achtung der Nutzer ist juenger als 18.")
        print("Ich bin immer noch innerhalb der if-Anweisung")
        age = 99
    
    print("Programmende")

# ex_11 if-Anweisung mit elif- und else-Zweigen erweitern
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_11 if-Anweisung mit elif- und else-Zweigen erweitern'"
    "\r\n")    
    
    age = int(input("Bitte gebe dein Alter ein: "))
    
    if age  < 18:
        print("Achtung der Nutzer ist juenger als 18.")
    elif age == 18: print("Der Nutzer ist exakt 18.")        
    elif age == 19:
        print("Der Nutzer ist exakt 19 Jahre alt.")
    else:
        print("Der Nutzer ist volljaehrig.")
        
    print("Programmende")

# ex_12 Logische Operatoren
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_12 Logische Operatoren'"
    "\r\n")
    
    print("Willkommen in der Lotterie!")
    number1 = int(input("Bitte waehle eine Zahl zwischen 1 und 49: "))
    number2 = int(input("Bitte waehle eine Zahl zwischen 1 und 49: "))
    number3 = int(input("Bitte waehle eine Zahl zwischen 1 und 49: "))
    
    # Gewinnzahl 1: 3
    # Gewinnzahl 2: 14
    # Gewinnzahl 3: 22

    if number1 == 3 and number2 == 14 and number3 == 22:
        print("Herzlichen Glueckwunsch, du hast die Lotterie gewonnen!")
    else:
        print("Du hast leider verloren ...")

# ex_13 Die while Schleife
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_13 Die while Schleife'"
    "\r\n")

    counter = 5
    while counter < 10:
        counter += 1
        print(f"Hier steht Code, der wiederholt {{{counter}}} ausgefuehrt werden soll.")

# ex_14 Einführung in Listen
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_14 Einfuehrung in Listen'"
    "\r\n")

    test_variable = 10
    numbers = [3,5,15,17,20] # [Wert1, Wert2, Wert3, ..., WertN]
    
    print(numbers)
    print(type(numbers))
    
    print("\r\n")

    names = ["Janek", "Hendrik", "Fritz", "Tanja", "Susi", 4, 8.2] # Alle (darstellbare) Typen können gemischt beinhaltet werden.
    print(names)
    print(type(numbers))

# ex_15 Zugriff auf Listen
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_15 Zugriff auf Listen'"
    "\r\n")

    names = ["Janek", "Hendrik", "Fritz", "Tanja", "Susi", 4, 8.2]
    print(names)
    
    counter = 0
    while counter < 7:
        counter += 1
        print(f"+{counter}. Listeneintrag: '{names[counter-1]}'")
        print(f"{-counter}. Listeneintrag: '{names[-counter]}'")

    names[0] = "Xaver"
    print(names)

# ex_16 Die for Schleife
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_16 Die for Schleife'"
    "\r\n")

    for element in [1,3,5,7]:
        print(element)
    print("\r\n")
    for element in "Ich bin ein String.":
        print(element)

# ex_17 for Schleife als Zählerschleife verwenden
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_17 for Schleife als Zaehlerschleife verwenden'"
    "\r\n")
    
    for element in range(5, 10+1, 2):
        print(element)

# ex_18 Funktionen
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_18 Funktionen'"
    "\r\n")
    
    print("Das ist eine Ausgabe.")
    # say_hello()    # Fehler, da Funktion vor Definition aufgerufen wird, da der Interpreter noch nichts davon weiß.
    def say_hello():
        print("Hallo, Hendrik.")
        print("Willkommen zurueck.")
    
    say_hello()
    print("Test")
    say_hello()

# ex_19 Funktionen mit Parametern
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_19 Funktionen mit Parametern'"
    "\r\n")
        
    def say_hello(first_name, last_name):
        print("Hallo, " + first_name + " " + last_name + ".")
        print("Willkommen zurueck.")
    
    say_hello("Hendrik", "Hendrikson")
    say_hello("Fritz", "Bauer")
    say_hello("Susi", "Mustermann")
    
# ex_20 Funktionen mit Rückgabewert
if (b_exec_all):
    print(str_trennlinie)
    print("'# ex_20 Funktionen mit Rueckgabewert'"
    "\r\n")
    
    def say_hello(first_name, last_name):
        print(print("Hallo, " + first_name + " " + last_name + "."))
        print("Willkommen zurueck.")
    
    print(type(say_hello("Hendrik", "Hendrikson"))) # erst innere Wert und dann äußere Wert wird ausgegeben # none == no return
    
    def maximum(a,b):
        if a < b: return b
        else: return a
    
    print("\r\n")
    result = maximum(3,7)
    print(result)
    
# ex_22 Klassen und Objekte
# ex_23 Der self Parameter
if (True):
    print(True)
    print("'# ex_22 Klassen und Objekte'"
    "\r\n"
    "'# ex_23 Der self Parameter'"
    "\r\n")

    class Car:
        def __init__(self):
            self.car_brand = None
            self.horse_power = None
            self.color = None
    car1 = Car()                    # Car Objekt 1
    print(car1.car_brand)
    car1.car_brand = "Audi"
    car1.horse_power = 258
    car1.color = "Blau"
    
    print(car1.car_brand)
    print(car1.horse_power)
    print(car1.color)
    
    car2 = Car()                    # Car Objekt 2
    print(car2.car_brand)
    car2.car_brand = "BMW"
    car2.horse_power = 210
    car2.color = "Schwarz"
    
    print(car2.car_brand)
    print(car2.horse_power)
    print(car2.color)
    
    print(car1)
    print(car2)



    

# ...



