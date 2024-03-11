#Slowniki = {} => mapa klucz-wartosc !!!!!!!!!!!

map = {'klucz': 'wartosc'}

alien_0 = {'color': 'zielony', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#klucz jest indeksem
#wartoscia moze byc dowolny obiekt
#struktura dynamiczna

#dodawanie nowych wartosci
alien_0['x_pos'] = 25
alien_0['y_pos'] = 25

#pusta deklaracja
mapa = {}

#zmiana wartosci
alien_0['x_pos'] = 30

#usuwanie klucz-wart
del alien_0['x_pos']

#formatowanie 
alien_1 = {
    'color': 'zielony', 
    'points': 5
    }

#metoda get() -> 2. arg domysl wart jesli nie znajdzie klucza
alien_1.get('color', 'Nie ma koloru xd')

#iteracja
#items() -> zwraca liste
for k, v in alien_1.items():
    print(f"klucz: {k} wart: {v}")

#keys() - zwraca klucze
#domyslna iteracja jest przez klucze wiec for key in "keys" // ale mozna tez keys()
for key in alien_0:
    print(key)

friends = {
    'Pawel': 24, 
    'Macias': 15
    }

if 'Pawel' in friends.keys():
    print('Pawel to real bro')

#sprawdza po kolejnosci ich wstawienia do slownika
#sortowanie kluczy
for key in sorted(friends.keys()):
    print(f'{key}')

#values() -> zwraca wart w slowniku (mapie)

#Zbior unikatowych wartosci -> set()
#DEKLARACJA SET 
#Trzeba mu odrazu dostarczyc wartosci: nie klucz-wartosc     
zbiorSet = {'python', 'python', 1, 2}
print(zbiorSet)

#PUSTA DEKLARACJA
zbSet = set()

#metoda zamieniajaca zbior na set
for friend in set(friends.keys()):
    print(friend)

#Zagniezdzanie -> listy w slowniku, slowniki w slownikach itd
#powinny miec te sama strukture 
    
aliens = [alien_0, alien_1]

fav_lang = {
    'os1': ['c++', 'java'],
    'os2': ['c++', 'python']
}

#jesli zagniezdzamy za bardzo to znaczy, ze da sie prosciej to zapisac

#slownik w slowniku
#grupa uzytkownikow 

users = {
    'id1': {
        'name': 'jns',
        'surname': 'sss'
    },
    'id2': {
        'name': 'jns2',
        'surname': 'sss2'
    },
    
}

