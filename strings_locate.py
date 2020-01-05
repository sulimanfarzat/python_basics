'''
Created on Jan 5, 2020

@author: suliman farzat

search a substring in string (locate_first, locate_all)
'''

def locate_first(string, sub): 
    index = 0
    while index < (len(string) - len(sub) + 1):
        if string[index : index + len(sub)] == sub:
            return index
        index += 1
    return -1

print(locate_first('cookbook', 'ook'))
print(locate_first('all your bass are belong to us', 'base'))




def locate_all(string, sub):
    matches = []
    index = 0
    while index < len(string) - len(sub) + 1:
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches

print(locate_all('cookbook', 'ook'))
print(locate_all('all your bass are belong to us', 'base'))
print(locate_all('yesyesyes', 'yes'))
