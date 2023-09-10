#Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
#After five failed attempts the program prints out Access denied. The correct username is python and password rules.

user = "python"
pass_word = "rules"


input_count =0
while input_count < 5:
    userid = input("enter your username")
    pw = input("enter your password")

    if userid == user and pw == pass_word:
        print("Welcome")
        break
    else:
        print("Try again")
        input_count = input_count+1
if input_count == 5:
    print("access denied")
