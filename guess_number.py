'''
Created on Jan 5, 2020

@author: suliman farzat

Number Guessing Game! with while 
'''


def prombet(numb):
    # Use this function to ask the user about a guess.
    # This function returns 'H', 'L', or 'C' (high, low or center).
    print(f"My guess: {numb}")
    inp = ""
    while inp.upper() not in ['H', 'L', 'C']:
        inp = input(f"Is {numb} too (H)igh, too (L)ow or (C)enter")
    return inp.upper()



def play(maxx):
    print(f"Think of a number from 1 to {max}.")
    input("When you're ready, press Enter.")
    high = maxx 
    low =1
    done = False
    count = 0
    
    while high != low and not done:
        count += 1
        guess = int((high + low) / 2)
        inp = prombet(guess)
        if inp == 'H':
            high = guess
        elif inp == 'L':
            low = guess
        else:
            done = True
            print(f"I'm guessed it in {count} guesses.")

    if high == low and not done:
        print("I'm confused! You ruled out all the numbers.")
  
  
    
if __name__ == '__main__':
    play(1000)