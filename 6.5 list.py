#Write a function that gets a list of integers as a parameter.
#The function returns a second list that is otherwise the same
#as the original list except that all uneven numbers have been removed.
#For testing, write a main program where you create a list, call the function,
#and then print out both the original as well as the cut-down list.

start = int(input("enter minimum"))
End = int(input ("enter Maximum"))

full_list = list(range(start, End+1, 1))
print(f"The complete list is {full_list}")

even = []
for i in full_list:
    if i%2 == 0:
        even.append(i)
print(f" the list of even numbers is {even}")
