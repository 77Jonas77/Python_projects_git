import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
words_dict = {}

# for index, row in data.iterrows():
#     letter = row[0]
#     word_for_letter = row[1]
#     words_dict[letter] = word_for_letter

words_dict = {row[0]: row[1] for index, row in data.iterrows()}

word = input("Type your word: ")

# for letter in word:
#     print(words_dict[letter.upper()])

output_list = [words_dict[letter] for letter in word]
