'''
PEDAC

P - Even word is a word that has letters show up an even number of times. pool would be 2 letters, because p and l show up once, making it not an even word. IT IS NOT BASED ON HOW MANY LETTERS IN TOTAL.

E - print(even_word('aaaa') == 0)
    print(even_word('potato') == 2)
    print(even_word('aabbbb') == 0)
    print(even_word('aaabbbccc') == 3)

D - Dictionary

A - 1. Create new dictionary called chars, to store letters, and a counter to store number of letters to remove
    2. Loop over given string
        a. For every letter in the string, store it in chars if it is not there and initialize with 1, otherwise add 1 if it shows up again
    3. Loop over dictionary
        a. For every key in the dictionary, check its value. If the value is not an even number, add to counter
'''


def even_word(string):
    chars = {}
    total = 0

    for letter in string:
        if letter not in chars:
            chars[letter] = 1
        else:
            chars[letter] += 1

    for key, value in chars.items():
        if value % 2 != 0:
            total += 1

    return total