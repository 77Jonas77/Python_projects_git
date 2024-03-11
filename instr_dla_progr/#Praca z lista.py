#Praca z lista

#Petla for
cars = ['Audi', 'Bmw', 'McClaren']

for car in cars:        #liczba_pojedyncza dla elementu        
    print(car)

#Listy liczbowe 
#Funkcja range() -> generowanie serii liczb 

for val in range(1,5):       #1, 2, 3, 4
    print(val, end = ' ')

#range(6) -> 0, 1, 2, 3, 4, 5
#list() -> konwersja zbioru na liste
#list(range(1,5))
#3 argument (krok) -> range(2,11,2) -> liczby parzyste od 2 do 10

#Proste dane stat dot listy liczb
#min() // max() // sum() //argumentami sa listy / zbiory

print()
print(min({0,1,2,3,4}))

#Lista skladana!
squares = [value**2 for value in range(1,11)]

#myList = [value for value in range (1,100_000_001)]
#print(min(myList), max(myList))

#Wycinek listy (slice)
players = ['Lewy', 'Piszczu', 'Reus']
print(players[0:2])     #[pocz:koniec]
print(players[:2])      #zacznie od pocz jak sie pominie
print(players[1:])      #adekwatnie do konca
print(players[-2:])     #MOZEMY DOWOLNIE WYSWIETLAC LISTE 
print(players[:-1])

#3. ARGUMENT -> KROK list[pocz:kon:krok]
print(players[-3::2])       #Zaczynamy od 3 od konca, idziemy do konca, o ile krokow

playersMain = [
    'Lewy', 'Piszczu', 'Reus', 'Krycha'
]

for player in playersMain[:-1]:
    print(f"{player}  dostaje powolanie do kadry")

#Kopiowanie zawartosci listy
my_fav_food = ['pizza', 'makaroni', 'kebab', 'bialeczko']
fav_ziomka = my_fav_food[:]

#TO NIE DZIALA -> w sensie dziala, ale teraz obie zmienne (etykiety) wskazuja na ten sam obiekt
#my_fav_food = fav_ziomka

#4.10
my_fav_food = ['pizza', 'makaroni', 'kebab', 'bialeczko', 'witaminki']

print(my_fav_food[:3])      #3 pierwsze
print(my_fav_food[len(my_fav_food)//2::])       #3 w srodku
print(my_fav_food[-3::])        #3 last

#4.11
my_fav_food.append('Pepperoni')
for food in my_fav_food:
    print(food)

#Krotka - lista el ktore nie moga sie zmienic (niemodyfikowalna)  ==> () tuple
dimentions = (200, 50)
print(dimentions[0])

#dimentions[0] = 30 ==> blad
#JEST DEFINIOWANA PO UMIESZCZENIU PRZECINKA W NAWIASIE 
my_t_1size = (2,)
#1 EL MUSI MIEC PRZECINEK

#zmiana mozliwa tylko poprzez ponowne definiowanie
my_t_1size = (2,3,4,5,)     #co ciekawe ten przecinek nic nie zmienia
print(my_t_1size)

#STYL TWORZONEGO KODU
#PEP -> Python Enhancement Proposal 

#Wciecia -> 4 spacje
#Dlugosc 79 (kom - 72)      
#Puste wiersze - oszczednie
