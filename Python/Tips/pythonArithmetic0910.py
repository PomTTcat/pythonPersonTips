# -*- coding: utf-8 -*-


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])



print duplicate_encode('abcdcd')


word = 'AADHKDHKAXB'
a = word.lower
print a
# print word.lower().count('f')