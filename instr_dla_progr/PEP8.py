#== Zen Pythona ==

#Piękne jest lepsze niż brzydkie.
#Wyrażone wprost jest lepsze niż domniemane.
#Proste jest lepsze niż złożone.
#Złożone jest lepsze niż skomplikowane.rect
#Płaskie jest lepsze niż wielopoziomowe.
#Rzadkie jest lepsze niż gęste.
#Czytelność się liczy.
#Sytuacje wyjątkowe nie są na tyle wyjątkowe, aby łamać reguły.
#Choć praktyczność przeważa nad konsekwencją.
#Błędy zawsze powinny być sygnalizowane.
#Chyba że zostaną celowo ukryte.
#W razie niejasności powstrzymaj pokusę zgadywania.
#Powinien być jeden -- i najlepiej tylko jeden -- oczywisty sposób na zrobienie danej rzeczy.
#Choć ten sposób może nie być oczywisty jeśli nie jest się Holendrem.
#Teraz jest lepsze niż nigdy.
#Chociaż nigdy jest często lepsze niż natychmiast.
#Jeśli rozwiązanie jest trudno wyjaśnić, to jest ono złym pomysłem.
#Jeśli rozwiązanie jest łatwo wyjaśnić, to może ono być dobrym pomysłem.
#Przestrzenie nazw to jeden z niesamowicie genialnych pomysłów -- miejmy ich więcej! 

#== PEP8 ==
#4 spaces per identation (wciecie) level

#if too long 
#if (this_is_one_thing and
#    that_is_another_thing):
#    do_something()

#closing brackets etc. 
#my_list = [
#    1, 2, 3,
#    4, 5, 6,
#    ]

#max line length = 79 -> limit line length

#break before or after a binary operator as long as convention is consistent locally
#income = (gross_wages
#          + taxable_interest
#          + (dividends - qualified_dividends)
#          - ira_deduction
#          - student_loan_interest)

#Blank lines
#Surround top-level function and class definitions with two blank lines.
#Method definitions inside a class are surrounded by a single blank line.
#Ommited between a bunch of related one-liners
#==> use blank lines in functions, sparingly, to indicate logical sections

#Source file encoding -> UTF-8 and dont have encoding declaration
#Other non-ASCII characters sparingly!

#Imports 
#separate lines 
#from subprocess import Popen, PIPE
#Imports should be grouped in the following order:
#===
#Standard library imports.
#Related third party imports.
#Local application/library specific imports.
#===
#Absolute imports are recommended -> readable
#import mypkg.sibling
#from mypkg import sibling

#Module level dunder names
#__future__ before rest but after module docstring but before any import 
#rest (before imports aw) __all__ // __version__ // __author__

#Whitespaces - in general be careful with whitespaces
#Avoid extraneous whitespace in the following situations:
#spam( ham[ 1 ], { eggs: 2 } ) ==> spam(ham[1], {eggs: 2})
#if x == 4 : print(x , y) ; x , y = y , x ==> if x == 4: print(x, y); x, y = y, x
#etc

#Trailing commas 
#The pattern is to put each value (etc.) on a line by itself, 
#always adding a trailing comma, and add the close parenthesis/bracket/brace on the next line.
## Correct:
#FILES = [
#    'setup.cfg',
#    'tox.ini',
#    ]
#initialize(FILES,
#           error=True,
#           )

#COMMENTS 
#keep comments up-to-date when the code changes

#Inline comments
#An inline comment is a comment on the same line as a statement. 
#Inline comments should be separated by at least two spaces from the statement.
#They should start with a # and a single space.
#x = x + 1                 # Compensate for border

#DOCUMENTATION STRINGS
#Write docstrings for all public modules, functions, classes, and methods. 
#Docstrings are not necessary for non-public methods, 
#but you should have a comment that describes what the method does. 
#This comment should appear after the def line.

#MULTILINE
#"""Return a foobang
#
#Optional plotz says to frobnicate the bizbaz first.
#"""

#ONELINER
#"""Return an ex-parrot."""

#CamelCase etc
#There’s also the style of using a short unique prefix to group related names together. 

#Never use the characters 
# ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye)
#as single character variable names.
#for some fonts -> unreadable

#packeges -> all-lowercase names
#class, type variable -> CapWords
#exceptions -> Error suffix
#functions -> lowercase with wordsd separater by underscores (variables as well)

#Always use self for the first argument to instance methods.
#Always use cls for the first argument to class methods.

#Generally, double leading underscores should be used only to avoid name conflicts 
#with attributes in classes designed to be subclassed.

#Constants -> MAX_OVERFLOW (CAPITAL LETTERS)

#!private -> non-public (no atribute is really private in Python)
#subclass API ("protected" in Java eg)

#comparisons to singletones like None using is or is not // not ==
#Code should be written in a way that does not disadvantage other implementations 

#eg a+=b or a=a+b (string) -> use parts of the library
#is not (correct) than not is

#Always use a def statement instead of an assignment statement 
#that binds a lambda expression directly to an identifier:
#def f(x): return 2*x (correct)
#f = lambda x: 2*x (wrong)

#Exception > BaseException
#while catching exceptions mention specific exceptions
#limit try clause to the absolute minimum amount