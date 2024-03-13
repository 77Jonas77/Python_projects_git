#Funkcje

#Definiowanie funkcji + docstring
def hello():
    """Wyswietlenie prostego przywitania"""
    print('Siemanko')

hello()

#dowolna wartosc na arg
def hello_user(username):
    """Przywitanie z usernamem"""
    print(f'Siemanko {username}')

hello_user(2)
hello_user('user')

#arg pozycyjne -> kolejnosc ma znaczenie

def hello_pet(pet1, pet2):
    print(f"{pet1} {pet2}")

hello_pet("uno", 'dos')

#w postaci slow kluczowych -> klucz-wartosc 
#-> nie ma kolejnosci / okreslamy dokladnie wart arg:

hello_pet(pet2="uno", pet1='dos')     #dla tych samych da arg repeated (syntax)

#ustaw wart domyslnej dla arg

def hello_pet(pet1, pet2='domyslna'):
    print(f"{pet1} {pet2}")

#trzeba zainicjowac arg, ktory nie ma domyslnej bo bd blad / 
#zmieniajac wart argumentow i pozycje mozemy nie podawac np nic (albo te bez domyslnych i tyle)
hello_pet('x')  
hello_pet(pet1 = 'x')

#zwrotna wart za pomoca return

def suma3(l1 = 0, l2 = 0, l3 = 0):
    return l1+l2+l3

print(suma3(1,2,3))

#opcjonalnosc arg
def full_name(imie, nazwisko, dr_imie=''):
    return f"{imie} {dr_imie} {nazwisko}"

print(full_name('Jonasz', 'ek'))
print(full_name('Jonasz', 'ek', 'xd'))

#None -> wart specjalna, gdy zmiennej nie zostanie przypisana zadna wartosc 
#(w wyr warunkowym) -> daje False

def print_cos(unprinted_cos):
    """
    DOCSTRING ALE DLUZSZY DOCSTRING ALE DLUZSZY DOCSTRING ALE DLUZSZY
    DOCSTRING ALE DLUZSZY DOCSTRING ALE DLUZSZY DOCSTRING ALE DLUZSZY
    DOCSTRING ALE DLUZSZY DOCSTRING ALE DLUZSZY DOCSTRING ALE DLUZSZY
    """
    print("whatever")

print_cos("xd")

#dzialanie na kopii struktury: -> bo inaczej na tym samym obiekcie!
#def nazwa_funkcji(nazwa_listy[:]):

#dowolna liczba argumentow -> tworzymy pusta krotke o nazwie toppings
#nawet dla 1 wartosci przyjmie

def make_pizza(*toppings):
    print(toppings[:])

make_pizza('xddd','xddd2')
make_pizza('xddd')

#taki arg musi znajdowac sie na koncu definicji funkcji
#dowolna liczba arg w postaci slow kluczowych
#user_info -> pusty slownik -> przyjmujemy dowolna liczbe arg w postaci (k: w)

def build_profile(name, surname, **user_info):
    user_info['first_name'] = name;
    user_info['last_name'] = surname;
    return user_info

user_profile = build_profile('jns', 'soj', location='wwa', field='IT')

print(user_profile)
    
#przechowywanie funkcji w modulach -> innym pliku

#import modulu:
#import nazwa_modulu

#okresl funkcji
#nazwa_modulu.nazwa_funkcji()
#from nazwa_modulu import nazwa_funkcji

#wielu:
#from nazwa_modulu import nazwa_funkcji_0, nazwa_funkcji_1, nazwa_funkcji_3

#uzywanie aliasow funkcji (as)
#from nazwa_m import nazw_f as alias 
    
#uzywanie aliasow modulow     
#import nazwa_modulu as xd
#xd.nazwa_m()

#import wszyst funkcji modulu
#from nazwa_m import *

#NAZWY FUNKCJI - zasady

#male litery 
#znaki podkreslenia
#kom wyjasniajacy dzialanie tuz po definicji (docstring)
#dla wart domyslnej nie ma spacji -> to samo w przypadku slow kluczowych(wyw met)
#2 puste wiersze oddzielajace funkcje w module
#import na pocz (albo po kom opisujacych przeznaczenie programu / modulu)