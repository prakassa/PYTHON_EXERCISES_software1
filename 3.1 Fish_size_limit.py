#Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

fish_caught = float(input("How many centimeters is the size of the Zander?"))
if fish_caught<= 42:
    print("Release the fish back to the lake. It is", (42-fish_caught), "cms below  limit. Try again")
else: print("Good! lucky day.")