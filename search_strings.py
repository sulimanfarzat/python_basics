'''
Created on Jan 5, 2020

@author: suliman farzat

search a substring in string
'''


word = "cookbook"
print(word[4])

location = 5
size = 3
print(word[location : location+size])


# start with
def starts_with_v1(long, short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True
    
def starts_with_v2(long, short):
    length = len(short)
    beginning = long[0 : length]
    if beginning == short:
        return True
    else:
        return False
    
def starts_with_v3(long, short):
    return long[0:len(short)] == short

# return true  
v1 = starts_with_v1('bob newby', 'bob')
v2 = starts_with_v2('bob newby', 'bob')
v3 = starts_with_v3('bob newby', 'bob')
print(v1, v2, v3 )

# return false
v1 = starts_with_v1('electric bill', 'bill')
v2 = starts_with_v2('electric bill', 'bill')
v3 = starts_with_v3('electric bill', 'bill')
print(v1, v2, v3 )
