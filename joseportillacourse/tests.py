# st = 'Print only the words that start with s in this sentence'
# list_splitted = st.split()
#
# for word in list_splitted:
#     if word[0] == 's' or word[0] == 'S':
#         print(word)
#
# for num in range(0, 11, 2):
#     print(num)
#
# for num in range(0, 11):
#     if num % 2 == 0:
#         print(num)
#
#
# my_list = [x for x in range(1, 51) if x % 3 == 0]
# print(my_list)
#
# st = 'Print every word in this sentence that has an even number of letters'
# my_words = st.split()
#
# for word in my_words:
#     if len(word) % 2 == 0:
#         print("even!")
#
# for x in range(1, 101):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 5 == 0:
#         print("Buzz")
#     elif x % 3 == 0:
#         print("Fizz")
#
# st = 'Create a list of the first letters of every word in this string'
#
# first_letters = [word[0] for word in st.split()]
# print(first_letters)
import string


def vol(rad):
    print((4 / 3) * 3.14 * rad ** 3)


def ran_check(num, low, high):
    if low <= num <= high:      # num in range(low,high +1)
        print(f"{num} is in range between {low} and {high}")


def up_low(s):
    count_upper = 0
    count_lower = 0
    for letter in s:
        if letter.isupper():
            count_upper += 1
        elif letter.islower():
            count_lower += 1
    print(count_upper, count_lower)


def unique_list(lst):
    unique_lista = set(lst)
    print(unique_lista)


def unique_list2(lst):
    unique_lista = []
    for num in filter(lambda x: x not in unique_lista, lst):
        unique_lista.append(num)
    print(unique_lista)


unique_list2([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply([1, 2, 3, -4]))


def check_palindrom(s):
    s.replace(' ', '')
    return s == s[::-1]


print(check_palindrom('helleh'))


def ispangram(str1, alphabet=string.ascii_lowercase):
    set_alph = set(alphabet)
    str1 = str1.s.replace(' ', '')
    str1 = str1.lower()
    str1 = set(str1)

    return str1 == set_alph


print(ispangram("The quick brown fox jumps over the lazy dog"))
