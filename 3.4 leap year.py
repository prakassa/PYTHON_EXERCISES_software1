#Write a program that asks the user to enter a year
#and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.

year= int(input("which year you want to check?"))

if year%4 == 0:
    print("yes it is the leap year")
else:
    print("No it is not a leap year")