'''
Created on Jan 4, 2020

@author: suliman farzat

mutable and immutable
'''

# immutable: unchangeable
noun = "wolf" 
#noun[0] = "g"
print(noun)


# mutable: changeable
bunch = ['banana', 'banana', 'banana']
bunches = [bunch, bunch, bunch]
for b in bunches:
    print(b)
print("------------------") 
   
bunches[0][0] = 'orange'   
for b in bunches:
    print(b)