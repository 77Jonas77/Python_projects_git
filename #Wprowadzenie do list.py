#Wprowadzenie do list
 
#Czym jest lista?
#Lista to kolekcja el. ulozonych w okreslonej kolejnosci. 
#Nazwa zazwyczaj w liczbie mnogiej

#Implementacja myList = [] !!!nawiasy kwadratowe
#print(myList) ==> ['el1', 'el2', 'el3']

myList = [ 
    0, 1, 2,
    'nwm', 'ok'
]

print(myList)       #z naw kw 

#Indeksowanie myList[0]
print(myList[0])        #bez nawiasow kwadratowych (sama zawartosc)
print(myList[3].upper())        #dla danych typu int wywola blad (AttributeError)

print(myList[-1])       #ZWRACA OSTATNI ELEMENT LISTY! itd
msg = f"{myList[-1].upper()} zrobie to"
print(msg)

#Manipulacja danymi
#Wiekszosc list jest dynaczmiczna -> zmienia sie jej zawartosc w trakcie dzialania programu
#Zamiana / Wstawianie wartosci

myList[0] = "Hyundai"

#Dodawanie el (na koniec)
myList.append('Siemano')

#Dodanie el (na dowolny indeks)
myList.insert(0, 'BMW')

#Usuniecie el (z pocz) // nie uzyskujemy dostepu do wartosci
del myList[0] 

#Usuniecie el (z konca - bez arg) // (dowolny arg - podajac indeks) // uzysk dost
deleted_el = myList.pop()
deleted_el = myList.pop(2)
print(f"{deleted_el} popped" )

#Usuwanie el znajac jego wartosc -> USUWA TYLKO 1 ZNALEZIONY PASUJACY EL
myList.remove('Hyundai')

guestList = []
guestList.append('Elon Musk')
guestList.append('Mark Cukier')

print(f"{guestList[0]} I invite u for my bd party ;)")
print(f"{guestList[1]} is busy that day so he can't attend")

guestList.remove('Mark Cukier')
#lub guestList.pop() // guestList.pop(1)

guestList.insert(0, 'Mamita')
guestList.insert(3,'Mamita')

deleted_guest = guestList.pop()
print(f"{deleted_guest} sorry no chairs left bsc of santa")

print(guestList)
del guestList[-1]
print(guestList)
del guestList       #usuwa cala liste

guestList = [ 
    'Audi', 'Pjatk', 'Bmw'
    ]

#Sortowanie listy -> trwale
guestList.sort()       #tylko dane tego samego typu by sie przydaly ;)
guestList.sort(reverse=True)       #Odwrotnie nie alfabetycznie (True/False duzymi)          

#Sortowanie listy -> nietrwale
print(sorted(guestList))       #reverse=True tez tutaj dziala

#Trzeba pamietac ze to bedzie dzialac tylko 
#w przypadku tych samych wielkosci liter na tym etapie!

#Odwracanie kolejnosci
guestList.reverse()        #odwrotnie po prostu // trwale ale mozna jeszcze raz reverse() (wtedy powrot)

#Dlugosc listy
print(len(guestList))

myList2 = ['Audi', 'Pjatk', 'Basen']
print(sorted(myList2))
print(sorted(myList2, reverse=True))

#Zwracaja NONE!
print(myList2.reverse())
print(myList2.sort())

