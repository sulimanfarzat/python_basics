'''
Created on Jan 5, 2020

@author: suliman farzat

search a substring in string (string methods)
'''


string = 'A Tale of Two Cities'

_find = string.find('Cities')
_count = string.count('o')
_lower = string.lower()
_upper = string.upper()
_endswith = string.endswith('Cities')
_split = string.split('Two', 1)
_startswith = string.startswith('A')

print(string)
print('Two' in string)
print('Two' not in string)
print(3 in [1, 2, 3, 4])
print([2, 3] in [1, [2, 3], 4])

print(_find)
print(_count)
print(_lower)
print(_upper)
print(_endswith)
print(_split)
print(_startswith)


lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

def breakify(strings):
    return '<br>'.join(strings)

print(breakify(lines))
