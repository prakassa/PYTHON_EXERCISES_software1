#Write a game where the computer draws a random integer between 1 and 10.
#The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text:
#Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random

draw = random.randint(1,10)
#print(draw)
guess = int(input("Guess your number"))

while draw != guess:
        if draw < guess:
            print("too high")
        elif draw > guess:
            print("too low")
        guess = int(input("Guess your number"))

print("correct")