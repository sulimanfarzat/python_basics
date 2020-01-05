'''
Created on Jan 5, 2020

@author: suliman farzat
'''

import random
from string_app import words
from _ast import If


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    position = 0

    # Add a while loop here.
    while position < len(template):
        if template[position: position + 8] == '{{noun}}':
            output.append(random.choice(nouns))
            position += 8
        elif template[position: position + 8] == '{{verb}}':
            output.append(random.choice(verbs))
            position += 8
        else:
            # Copy character to the output
            output.append(template[position])
            position += 1
        
        

    # After the loop has finished, Join the output into a single string.
    output = ''.join(output)

    # return the output.
    return output


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs, words.templates))
