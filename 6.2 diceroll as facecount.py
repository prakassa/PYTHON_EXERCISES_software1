import random

face_number = int(input("how many faces are in the dice?"))
def draw():
    return random.randint(1,face_number)

rolls= 0
while True:
    output = draw()
    print(output)
    rolls = rolls+1
    if output == face_number:
        break