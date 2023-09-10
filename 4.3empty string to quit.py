#Write a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.
lst= list()
number = input("Enter number")
while number != "":
    lst.append(int(number))
    number = input("Enter number")

print("stopped")


print("the biggest number is", max(lst))
print("the smallest number is", min(lst))