'''
Created on Jan 6, 2020

@author: suliman farzat
'''

no_list = [22,68,90,78,90,88]

def average(x):
    #complete the function's body to return the average
    _length = len(x[:])
    _sum = sum(x, 0) 
    return _sum / _length
    
print(average(no_list))



def maximum(no_list):
    #complete the function to return the highest number in the list
    return max(no_list)

print(maximum(no_list))
