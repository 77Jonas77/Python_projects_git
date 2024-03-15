#Klasy

class Car:
    """Klasa modelujaca samochod"""
    
    #konwencja __n__ dla metod specjalnych (nie kolidowaly metody domyslne z naszymi)
    #self - odwolanie do egzemplarza (musi byc na pocz) -> przekazany w fabryk
    #automatycznie
    #prefix self (this)
    #pola obiektowe -> atrybuty
    def __init__(self, model, marka):     #Konstruktor
        """Inicjalizacja atrybutow (pol klasowych / obiektowych / egzemplarza)"""
        self.model = model
        self.marka = marka
        self.przebieg = 0

    def ride(self):
        print(f"wrrrrrrum...!!! {self.przebieg}")

    def update_przebieg(self, przebieg):
        self.przebieg = przebieg


myCar = Car("M3", "BMW")

print(f"{myCar.marka} {myCar.model} {myCar.ride()}")        #metoda wysw sie 1?

#zmiana wartosci atrybutu
#bezposrednio
myCar.marka = "Audi"

#za pom metody
myCar.update_przebieg(123)

#inkrementacja - to samo ale dodajemy a nie setujemy wartosc

#Dziedziczenie - kl potomna i nadrzedna - dziedziczenie atryb i metod

#Kl nadrzedna w tym samym pliku (nadrzedna - super / superklasa stad super xd)
#overridowanie metod

class ElectricCar(Car):

    def __init__(self, model, marka):
        super().__init__(model, marka)      #fspecj wyw konstruk kl nadrz
        self.pojemnoscBaterii = 40

    def opiszBaterie(self):
        print(f"Poj bat wyn: {self.pojemnoscBaterii}")

    def ride(self):
        """Nie trzeba zadnych override?"""
        print("ja nie wrum ;(")


ec = ElectricCar("S", "Tesla")
ec.opiszBaterie()
ec.ride()

#Kompozycja - rozbicie klasy na kilka mniejszych wspolpracujacych ze soba
#np jesli duzo info o baterii, to tworzymy klase dla baterii i uzywamy 
#jako atrybutu

#import klas
#from car import Car
#from car import Car, ElectricCar
#import car
#from module_name import * //niezalecane, poniewaz nie ma jasnosci co do konkret 
#klas oraz w przypadku 2 takich samych klas tez nie jestesmy w stanie rozroznic
#===> nazwa_mod.nazwa_klasy (unikamy konfliktow nazw i wgl)

#modul w module -> tworzymy nowy modul z klas wymagajacych do dzialania 
#importu z innej klasy -> import Car do pliku electric_car.py (bateria/ec)
#import modulu w module (jak wyzej) -> najpierw import mod nadrz, pozniej podrz

#Aliasy
#from electric_car import ElectricCar as EC
#-> EC('nissan,'leaf', 2024)

#import nazwa_mod as ec
#-> my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)

#Biblioteka standardowa Pythona
#from random import randint
#randint(pocz,kon)

#choice(lista albo krotka) -> zwraca "losowo" wybrany element

#STYL KLASY
#Nazwa - CamelCase
#egzemplarze i atrybuty klas -> mala litera (miedzy _ dopuszczalne)
#docstring na pocz klasy
#na pocz metod
#metody - 1 pusty wiersz
#klasy - 2 puste wiersze
#moduly ze standardowej - 1 p wiersz od naszych


