#Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order. Hint:
#You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

lst=[]

number = input("enter a number")
while number != "":
    lst.append(number)
    number = input("enter a number")
#print(lst)

intiger_list = sorted([int(x) for x in (lst)])
intiger_list.reverse()

#print(intiger_list)
print("The greatest five numbers in descending order are:",(intiger_list[0:5]))

