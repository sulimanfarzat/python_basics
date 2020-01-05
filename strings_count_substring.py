'''
Created on Jan 5, 2020

@author: suliman farzat

search a substring in string
'''


def count_substring_v1(string, target):
    index = 0
    count = 0
    while index < (len(string) - len(target) + 1):
        if string[index : index + len(target)] == target:
            count += 1
        index += 1 # <- look here
    return count

print(count_substring_v1('love, love, love, all you need is love', 'love'))
print(count_substring_v1('AAAA', 'AA'))




def count_substring_v2(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
            index += len(target)   # <- look here
        else:
            index += 1
    return count

print(count_substring_v2('love, love, love, all you need is love', 'love'))
print(count_substring_v2('AAAA', 'AA'))
