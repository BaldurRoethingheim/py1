'''
This is a 
multi line 
comment.
'''
# this is a single line comment

# tutorial "https://www.youtube.com/watch?v=oxXAb8IikHM&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB"

# ex_1 Dein erstes Programm
print("--------------------------")
print("'# ex_1 Dein erstes Programm'"
"\r\n")

from os import name


print("Hey.\r\n"
      "How are you?")
def print_hi(name):
    print(f'Hallo, {name}.')    
if __name__ == '__main__':
    print_hi('Welt')    
print("Hallo Welt, ich lerne gerade programmieren.")

# ex_2 Zahlen in Python
print("--------------------------")
print("'# ex_2 Zahlen in Python'"
"\r\n")

print(-7)
print(8/4)
print((3+2)*(2-1))
print(2.1 + 1.5)
print(2.4*2)

# ex_3 Strings in Python
print("--------------------------")
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
print("--------------------------")
print("'# ex_4 Variablen'"
"\r\n")

num_age = 27
str_name = "Markus"
print(num_age)
num_age = 28
print(num_age)
print(str_name)

# ex_5 Datentypen int, float, str
print("--------------------------")
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
print("--------------------------")
print("'# ex_6 Die input()-Funktion'"
"\r\n")

print("Angfang des Programms")
str_name = input("Hinweis: Bitte deinen Namen einngeben:")
print("Meine Name ist " + str_name)
num_age = input("Hinweis: Bitte dein Alter einngeben:")
print("Mein Alter ist " + num_age)
print("Ende des Programms")

# ex_7 Type-Casting-Funktionen
print("--------------------------")
print("'# ex_7 Type-Casting-Funktionen'"
"\r\n")

value1 = input("Erste Zahle eingeben: ")
value2 = input("Zweite Zahle eingeben: ")

print(value1)
print(value2)
# ...



