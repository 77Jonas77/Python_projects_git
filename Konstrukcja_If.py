#Konstrukcja if
#and i or

#Sprawdzanie czy wartosc znajduje sie w liscie
cars = ['BMW', 'AUDI', 'MCCLAREN']

if 'BMW' in cars:
    print('BMW +')
else:
    print('BMW -')

if 'AUDI' in cars:
    print('a')
elif 'BMW' in cars:
    print('b')
else:
    print('Nothing')

#lepiej np nadawac wartosci tutaj i wyswietlac je za pomoca f"{wart}"
#mozna uzywac rowniez not w celu sprawdzenia czy np nie znajduje sie

for car in cars: 
    print(f"Kupuje sobie: {car}.")

#cars = []
#sprawdzenie czy lista nie jest pusta
if cars:
    for car in cars: 
        print(f"Kupuje sobie: {car}.")
else:
    print("Lista jest pusta")

available_cars = ['AUDI', 'MERCEDES']    

for car in cars: 
    if car not in available_cars: 
        print(f"{car} nie jest dostepny")

#PEP 8 -> spacje wokol operatorow porownania!
