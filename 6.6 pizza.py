#Write a function that receives two parameters:
#the diameter of a round pizza in centimeters and the price of the pizza in euros.
#The function calculates and returns the unit price of the pizza per square meter.
#The main program asks the user to enter the diameter and price of two pizzas
#and tells the user which pizza provides better value for money (which of them has a lower unit price).
#You must use the function you wrote for calculating the unit prices
R1 = (int(input("diameter 1:"))/2)/100
P1 = int(input("price 1:"))

R2 = (int(input("diameter 2:"))/2)/100
P2 = int(input("Price 2:"))
def unitprice(radius, price):
    return (f"The unit price is: {(price/(3.14 * (float(radius))**2))}")



first_rate = unitprice(R1 , P1)
print(f" {first_rate} per sq m for the first pizza")
second_rate = unitprice(R2 , P2)
print(f" {second_rate} per sq m for the second pizza")

if first_rate < second_rate:
    print(f"Go with the first one. it is better value for money ")
elif first_rate == second_rate:
    print("both are equally valued")
else:
    print("second one is better value for money")