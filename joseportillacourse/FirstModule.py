val = 3 + 7 + 90

print(type(val))

# string jest ordered

# slice ma otwarty nawias na tym co konczy
slowo = "essa77"
print(slowo[1:3:1])

# string jest immutable
# slowo[0] = 'P'  wywola blad
# Jak obejsc

new_word = slowo[1:3] + 'X'

# mozna mnozyc stringi

# interpolacja -> wstawianie zmiennej do stringa
result = 1.232323235566

print("{0} jest moim ulubionym".format(new_word))
print("{f} jest moim ulubionym".format(f=new_word))
print("{r:1.3f} jest moim ulubionym".format(r=result))  # :sz.precisonf
# print("{[0:3]} jest moim ulubionym".format(new_word))


# f-string python 3.6
print(f"{new_word}")
print(f"{new_word}")

my_list = [1, 2, 3, 4]
my_list2 = ["es", 1, 2]

print(len(my_list))
print(my_list2[::-1])  # odwrocenie

print(my_list[0])

my_list[0] = "xddd"

my_list.append("xdd2")
my_list.pop()  # ostatni i zwraca indeks
my_list.pop(2)  # na indeksie usuwa
another_list = my_list + my_list2
print(another_list)

# dictionaries - unordered / mutable

my_dict = {'key1': 23, 'key2': '55'}
print(my_dict['key1'])

t = ('a', 'b', 'a')
print(t.count('a'))
print(t.index('a'))

# sets - unordered / unique / mutable

my_set = set()
my_set.add(1)
print(my_set)

# my_set = set(dict)
# print(my_set)

b = None

# I/O
my_file = open("/Users/jonaszsojka/python_projects/JosePortillaCourse/text.txt")
file_text = my_file.read()  # czyta caly plik do jednego str wraz z whitespacami

# zresetowac wskaznik w pliku aby czytac ponownie z pliku
my_file.seek(0)

file_lines_list = my_file.readlines()  # wciaz z whitespacami
my_file.close()  # niezamkniecie powoduje bledy

# with - alternatywa dla plikow
with open(
        "/Users/jonaszsojka/python_projects/JosePortillaCourse/text.txt") as my_file_dwa:
    contents = my_file_dwa.read()
    # nie trzeba sie martwic o zamkniecie

# with open('/Users/jonaszsojka/python_projects/JosePortillaCourse/text.txt',
#          mode='w') as myfx:  # ale mozemy tylko pisac
#    my_file_dwa.write("xd")

# mozna tez append jako 'a'
# 'w+' - writing and reading (ale overwrite istniejacych plikow lub tworzenie nowych)
# 'r+' - w + r

x = "str" == "str"
print(x)

# or not and

# petle

# for
# jesli nie chcesz zmiennej z petli to uzywasz for _ in listaX:

# unpacking

myList = [(1, 2), (2, 3)]
for (a, b) in myList:       # a, b
    print(b)

mydict = {'key1': 23, 'key2': 55}

for key, value in mydict.items():       # bo items() zwraca tuple
    print(key, value)

# jesli petla wykona sie poprawnie (bez break), to wykona sie else

val = 0
while val < 5:
    print(f"val : {val}")
    val += 1
else:
    print("val is out of range")    # wykona sie tez gdy while ani 1 sie nie wyk

# pass -> nic nie robi
# zamiast kom np

for item in mydict.items():
    pass        # zamiast syntax error (pozniej sie dorobi)


