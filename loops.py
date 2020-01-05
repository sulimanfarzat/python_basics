'''
Created on Jan 5, 2020

@author: suliman farzat

loops in lists and strings
'''

for x in "many words":
    print(x)
    
    
for i in ["many", "words"]:
    print(i)

   

# return count of "x"
def count_x(string):
    total = 0
    for x in string:
        if x == "x":
            total += 1
    return total
    
print(count_x("oxen and foxen all live in boxen"))



# return count of target
def count_ch(string, target):
    total = 0
    for ch in string:
        if ch == target:
            total += 1
    return total

print(count_ch("the goofy doom of the balloon goons", "o"))
print(count_ch("papa pony and the parcel post problem", "p"))
print(count_ch("this bunch of words has no", "e"))



# while and linear search
def count_ch2(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total

print(count_ch2("the goofy doom of the balloon goons", "o"))



def until_dot(string):
    index = 0
    while index < len(string) and string[index] != '.':
        # No dots yet, keep going.
        index += 1
    # We either found a dot or ran out of string.
    return string[:index]

print(until_dot("192.168.200.2"))
print(until_dot("No dots here"))




def until_dot2(s):
    for index in range(len(s)):
        if s[index] == '.':
            # A dot! Return everything up to here.
            return s[:index]
    # We ran out of string without seeing any dots.
    # Return the whole string.
    return s

print(until_dot2("192.168.200.2"))
print(until_dot2("No dots here"))
        


# infinite loop
def repeating():
    while True:
        print("Help! i am trapped in an infinite loop!")


def no_repeating():
    words = []
    while True:
        word = input("Tell me a word: ")
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words

print(no_repeating())




def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                # break   # does not do what we want!
                return f"{x} * {y} == 512"

print(find_512())



