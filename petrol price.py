"""print("Check if the number is prime number. Press '0' to stop.")
number = int(input("Enter your number"))

if number == 1:
    print(f"no {number} is not a prime number")

elif number > 1:
    for i in range(2,number):
        if number % i == 0:
            print(f"no {number} is not a prime number ")
            break
    else:
        print(f"yes {number} is a prime number")



print("Thank you! program stopped.")"""

consumption = 5/100
km = int(input("how many kms you want to drive: "))
litres = km * consumption
print(f" we need {litres:.2f} litres of fuel for the drive.")
def price(litres):
    eur = litres * 1.95
    return eur

print(f"we need {price(litres)} euros for the drive. ")

recheck = input("do you want to have another check")
while recheck != "NO":
    consumption = 5 / 100
    km = int(input("how many kms you want to drive: "))
    litres = km * consumption
    print(f" we need {litres:.2f} litres of fuel for the drive.")
    print(f"we need {price(litres)} euros for the drive. ")
    recheck = input("do you want to have another check")
print("program stopped")