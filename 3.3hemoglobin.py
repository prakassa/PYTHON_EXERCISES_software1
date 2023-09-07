#Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input("What is your biological gender (Male or Female?")
hemo = float(input("what is your hemoglobin value(g/l)"))
if (gender == "male"):
    if(134 <= hemo <=167):
        print("Your hemoglobin value is normal")
    elif(hemo > 167):
        print("your hemoglobin value is high")
    else:
        print("your hemoglobin value is low")
elif (gender == "female"):
    if(117 <= hemo <= 155):
        print("Your hemoglobin value is normal")
    elif(hemo > 155):
        print("your hemoglobin value is high")
    else:
        print("your hemoglobin value is low")
else:
    print("invalid input")
