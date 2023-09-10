#Write a program that asks the user how many dice to roll.
#The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

import random
numbers= []

n= int(input("how many dices you want to roll?"))
for _ in range(n):
    draw = random.randint(1,6)
    numbers.append(draw)
print("the draws are:",numbers)
print("the sum of the draws is:",sum(numbers))
