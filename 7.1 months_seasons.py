#Write a program that asks the user for a number of a month
#and then prints out the corresponding season (spring, summer, autumn, winter).
#Save the seasons as strings into a tuple in your program.
#We can define each season to last three months, December being the first month of winter.

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
seasons = ("spring", "summer", "autumn", "winter")


number_of_month = int(input("enter the number of month "))
month = months[number_of_month-1]

print(f" the {number_of_month}th month is {month}")

def season(month):
    if month in months[2:5]:
        print(f" it is {seasons[0]} season")
    elif month in months[5:8]:
        print(f" it is {seasons[1]} season")
    elif month in months[8:11]:
        print(f" it is {seasons[2]} season")
    else:
        print(f" it is {seasons[-1]} season")

    return
season(month)
