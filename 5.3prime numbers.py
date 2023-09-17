print("Check if the number is prime number. Press '0' to stop.")
number = int(input("Enter your number"))
while number != 0:
    if number == 1:
        print(f"no {number} is not a prime number")
    if number == 0:
        print(f"no {number} is not a prime number")
    elif number < 1:
        for i in range(2,number):
            if number % i == 0:
                print(f"no {number} is not a prime number ")
                break

    else:
        print(f"yes {number} is a prime number")

    number = int(input("Enter your number"))

print("Thank you! program stopped.")