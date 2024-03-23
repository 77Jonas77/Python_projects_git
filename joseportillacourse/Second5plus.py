from random import shuffle

# lista
lista = (range(0, 11, 2))

# indeksowanie w for za pomoca unpacking
word = "abcdefg"
mylist2 = [1, 2, 3]
mylist = ['a', 'b', 'c']

for indx, letter in enumerate(word):
    print(letter, indx)

# laczenie list i paruja z odpowiadajcymi im indeksami
# mozna wiecej niz 2
# DZIALA TYLKO DO WARTOSCI KTORE MOGA BYC ZPAROWANE (jak cos jest dluzsze
# to nie paruje)

print("=======")
for item in zip(mylist2, mylist):
    print(item)

list(zip(mylist, mylist2))

# uzywanie in do sprawdzenia wystapienia
# dziala tez na dictionary (np 345 in d.keys() / d.values())

shuffle(mylist2)
print(mylist2)

# list comprehention - splaszczanie petli
mylistx = []

for letter in 'hello':
    mylistx.append(letter)

# ==

mylistx = [letter for letter in 'hello']
mylistx = [x for x in range(0, 11)]
mylistx = [x ** 2 for x in range(0, 11)]
mylistx = [x for x in range(0, 11) if x % 2 == 0]  # if po petli

# z if / else raczej niezalecane dla czytelnosci jest robienie onelinerow

results = [x if x % 2 == 0 else 'Odd' for x in range(0, 11)]  # +else to na pocz

# mozna robic nested loops

results = [x * y for x in [2, 3, 4] for y in [1, 10, 1000]] # nested
