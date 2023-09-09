
#build a calculator
def suma(a,b,c):
    add = a+b+c
    return add
def product(a,b,c):
    pro = a*b*c
    return pro
def sub(a,b,c):
    subs = (a-b-c)
    return subs
def div(a,b,c):
    divs =(a/b/c)
    return divs

num1=int(input("What is your first number?\n"))
num2=int(input("what is your second number?\n"))
num3=int(input("And what is the third number?\n"))
choice = input("what is you want to do? choose 1 for addition, 2 for multiplication and 3 for subtraction.")
if choice == "1":
    print ("the sum is",suma(num1,num2,num3))
elif choice == "2":
    print("the product is", product(num1,num2,num3))
elif choice =="3":
    print("the subtraction is", sub(num1, num2, num3))
elif choice =="4":
    print("the division is:", div(num1,num2, num3))