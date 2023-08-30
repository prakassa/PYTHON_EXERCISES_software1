print("insert", end=" "),
talent=float(input("talent"))
print("insert", end=" ")
pound= float(input("pound"))
print("insert", end=" ")
lot = float(input("lot"))

gram=((talent*20*32*13.3)+(pound*32*13.3)+(lot*13.3))

modern_kg = int(gram//1000)
modern_gram= (gram%1000)

print("The weight in modern units:", modern_kg, " kilograms and", modern_gram, "grams")