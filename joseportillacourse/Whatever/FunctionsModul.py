from random import shuffle


# def name_of_fun(): -> lowercase with underscores / snake_casing

# dynamicznie typowane typy argumentow metod
# pass nie zwraca nic

def check_even_list(list_to_check=None):  # pozycyjne argumenty
    if list_to_check is None:
        list_to_check = []

    for element in list_to_check:
        if element % 2 == 0:
            return True
        else:
            pass
    return False


def shuffle_list(list_to_shuffle):
    shuffle(list_to_shuffle)


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Zgadnij gdzie (0,1,2): ")
    return guess


def myfuncargs(*args):  # tuple of arg
    print(args)  # tuuuuuple
    return sum(args)


GLOBAL_VARIAB = "XDD"



def myfunckwargs(**kwargs):  # tuple of arg
    print(kwargs)  # tuuuuuple
    if 'fruit' in kwargs:
        print('My fruit is {} '.format(kwargs['fruit']))


def old_macdonald(name):
    new_name = ""
    for i, letter in enumerate(name):
        if i == 0 or i == 3:
            new_name += name[i].upper()
        else:
            new_name += name[i]
    return new_name


def master_yoda(text):
    sentence = []
    words = text.split()
    for word in reversed(words):
        sentence.append(word)
    return sentence


def square(num):
    return num ** 2


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    else:
        return mystring[0]


def check_even(num):
    return num % 2 == 0

# zmiana globalnej zmiennej
def func():
    global GLOBAL_VARIAB
    GLOBAL_VARIAB = "xdddd"

# lambda expression
sqr = lambda num: num ** 2

my_nums = [1, 2, 3, 4, 5]

# filter (true/ false) -> zwraca elementy zwracajace True dla funkcji
for item in filter(check_even, my_nums):
    print(item)

# map stosuje funkcje na kazdym elemencie tablicy
for item in map(square, my_nums):
    print(item)

# albo: lista kwadratow argumentow
list(map(square, my_nums))
list(map(splicer, my_nums))

lista = [' ', 'O', ' ']
shuffle(lista)

# ala gra w zgadywanie gdzie jest O
print(lista)

# *args **kwargs / argument - keyword_argument -> nieskonczona liczba arg

print(old_macdonald('macdonald'))
print(master_yoda('I am home'))

# lambda
map(lambda num: num ** 2, my_nums)
filter(lambda num: num % 2 == 0, my_nums)
map(lambda word: word[0], ["a", "asd", "basd"])
map(lambda word: word[::-1], ["a", "asd", "basd"])

# legb - zasieg zmiennych itd (Local, enclosing function, global, built-in
# mozna zrobic tez funkcje w funkcji - widzi zmienne nadfunkcji potem globalne
