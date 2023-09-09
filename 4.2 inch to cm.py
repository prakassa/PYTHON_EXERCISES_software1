
print("convert inches to cms")

while True:
        inch = float(input("How many inches is it?"))
        if inch < 0:
                print("Program end")

        cm= inch*2.54

        if inch > 0:
                print("Ok, that will be", cm, "centimeters")
