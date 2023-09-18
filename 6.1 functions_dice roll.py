import random
def draw():
    return random.randint(1,6)

rolls= 0
while True:
    output = draw()
    print(output)
    rolls = rolls+1
    if output == 6:
        break
