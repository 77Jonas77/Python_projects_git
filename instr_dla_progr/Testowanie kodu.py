#Testowanie kodu
#biblioteka pytest
#narzedzie pip do instalowania pakietow zew

#TESTOWANIE FUNKCJI

#pytest
#test jednostkowy -> spr konkretnego aspektu dzialania funkcji
#zestaw testow -> kolekcja testow jednostkowych (w szerokiej gamie sprawdza)
#pelne pokrycie -> wszelkie mozliwe sposoby na jkie mozna uzywac funkcje

#nazwa pliku testowego rozp sie od test_ bo jak nakarze wykonanie testow
#to bib szuka po sufixach od test_

#nastepnie def funkcje testu

#wykorzystanie asercji - sprawdza czy wynik otrzymany z dzialania funkcji jest
#taki sam jak oczekiwany

#assert wynik_funkcji == 'Poprawna Odp'
#pytest uruchamia pliki testowe!

#teraz wystarczy w konsoli wpisac pytest i otrzymujemy wyniki dla naszych testow
#albo python -m pytest -> w katalogu w ktorym sa testy 
#kropka po nazwie pliku inf o zaliczeniu testu (kazda kropka - 1 test)

# F - NIEZALICZENIE

#TESTOWANIE KLASY
#assert == / != / a / not a / element in lista / element not in lista / ITD

#DANE TESTOWE -> tworzenie zasobow dla wielu testow 
#-> def funckji z dekoratorem @pytest.fixture // dyrektywa przed funkcja
#-> dyrektywa zmienia sposob dzialania funkcji 