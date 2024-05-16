#Create if else statement to see if user likes dogs

answer = input("Do you like dogs? (yes/no): ")

while (answer.capitalize() != "Yes") and (answer.capitalize() != "No"):
    answer = input("Invalid input! Enter Yes or No: ")
    
if answer.capitalize() == "Yes":
    print("I guess you like dogs!")

elif answer.capitalize() == "No":
    print("I guess you don't like dogs.")
