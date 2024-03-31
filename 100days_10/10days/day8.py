"""Szyfr cezara"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = r"""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


def encode(text, key):
    """encoding text"""
    ciphered_text = ""
    for char in text:
        if char.isalpha():
            position_shifted = (alphabet.index(char) + key) % 26
            new_char = alphabet[position_shifted]
            ciphered_text += new_char
        else:
            ciphered_text += char
    return ciphered_text


def decode(text, key):
    """decoding ciphered text"""
    ciphered_text = ""
    for char in text:
        if char.isalpha():
            position_shifted = (alphabet.index(char) - key) % 26
            new_char = alphabet[position_shifted]
            ciphered_text += new_char
        else:
            ciphered_text += char
    return ciphered_text


def caesar(text, key, operation):
    """caesar cipher (both)"""
    # ustalenie operacji
    if operation.lower() == 'encode':
        pass
    elif operation.lower() == 'decode':
        key *= -1
    else:
        print('invalid operation')
    # kodowanie
    ciphered_text = ""
    for char in text:
        if char.isalpha():
            position_shifted = (alphabet.index(char) + key) % 26
            new_char = alphabet[position_shifted]
            ciphered_text += new_char
        else:
            ciphered_text += char
    return ciphered_text


if __name__ == "__main__":
    print(logo)
    print(decode(encode("python jest sztos", 9), 9))
    print(caesar("python jest sztos?!", 9, 'encode'))
    print(caesar(caesar("python jest sztos?!!", 9, 'encode'), 9, 'decode'))
