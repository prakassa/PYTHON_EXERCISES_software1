
print("convert inches to cms")
inch = float(input("How many inches is it?"))

cm= inch*2.54

if inch > 0:
        count=int(input("how many times should i display?"))
        i=0
        while i < count:
                print("Ok, that will be", cm, "centimeters")
                i=i+1
if inch < 0:
        print("Program end")
else:
        print("Thank you for asking")