from pathlib import Path

#Pliki i wyjatki

#wczytanie calego pliku na raz
#modul z okr funkcjon to biblioteka 
path = Path("jakis.txt")
contents = path.read_text()     #dodaje pusty ciag (wysw w postaci pustego w)
print(contents.rstrip())        #usuwa whitespace'y po prawej stronie c. tekst.

#wzglednia sciezka dostepu katalog/plik.txt (ale to podkatalog projektu)
#bezwzgledna sciezka (to caly home/user/...)

#wiersz po wierszu

splited_lines = path.read_text().splitlines()

for line in splited_lines:
    print(line)

#zapisywanie danych w pliku
    
path = Path("/Users/jonaszsojka/python_git/PPY_python/instr_dla_progr/zapis.txt")
path.write_text("siemano")
path.write_text("siemano2")
path.write_text("siemano3")     #nadpisuje zawartosc pliku

#zapisujemy tylko ciagi tekstowe w pliku tekstowym (konwersja / rzutowanie str())
#jesli plik nie istnieje to zostanie utworzony
#to co chcemy zapisac do pliku trzeba wczesniej przygotowac bo nadpisuje

#WYJATKI

#obsluga za pomoca try-except
#wywolywany zostaje stos wywolan

try:
    answer = 20
except:
    print("Nie dziel przez 0!")
else:
    print(answer)

#kazdy frag kodu ktorego wyk alezy od formuly w try powinien znalezc sie w else
#split() ->dzieli ciag tekstowy (po whitespaceach)

#Ciche niepowodzenie -> nic nie robienie / brak reakcji
    
try:
    answer = 20
except:
    pass
else:
    print(answer)

#JSON - javascript object notation - forma zapisu danych 
#komunikacja miedzy roznymi programami
#import json
#json.dumbs() -> zamiana na ciag tekstowy zaw reprezentacje dla json
#json.loads() -> JSON -> obiekt Python'a
#path = Path(zapis.json)
#path.write_text(json.loads(lista_jakas)) ...
    
#Refaktoryzacja -> kod dziala, chociaz mozemy jeszcze go usprawnic przez podzial
#na funkcje itd // funkcja to pojedyncze zadanie
    
