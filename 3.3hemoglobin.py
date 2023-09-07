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
