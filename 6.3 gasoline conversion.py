volume_gallons = float(input("How many gallons"))

def conversion():
    return (volume_gallons * 3.7854)

while volume_gallons > 0:
    volume_litre = conversion()
    print(f" it is {volume_litre} litres.")
    volume_gallons = float(input("How many gallons"))

print("Conversion ended")