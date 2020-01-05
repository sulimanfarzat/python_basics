'''
Created on Jan 5, 2020

@author: suliman farzat

search a substring in string
'''

def is_substring(short, long):
    index = 0
    
    while index < (len(long) - len(short) + 1):
        if long[index : index + len(short)] == short:
            return True
        index += 1
    return False


print(is_substring('dab', 'abracadabra'))
print(is_substring('bad', 'abracadabra'))