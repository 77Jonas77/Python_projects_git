#Dane wejsciowe uzytkownika i petla while
#Konwersja (jak podam float to nie zadziala)
dane_wejsciowe = int(input("Podaj costam: "))
print(dane_wejsciowe)

#active = True
#while active:
#    print("idk")

#break i continue
#ctrl c do zamkniecia / zatrzymania okna wyjsciowego

conf_users = [
    'Asia', 'Basia', 'Eliza'
]

#dopoki lista nie bedzie pusta
while conf_users:
    print(conf_users.pop())

#usuwanie okreslonej wartosci
    while 'Basia' in conf_users:
        conf_users.remove('Basia')

