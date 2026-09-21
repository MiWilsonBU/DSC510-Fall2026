#DSC 510
#Week 2
#Programming Assignment Week 2: Create a receipt for customers ordering fiber optic cable
#Author Sean Schlosser
#2026/09/19

"""Fiber Cable Install Receipt and Cost Calculator
Asks for company name and the number of feet of fiber needed, then calculates the cost and then prints receipt
"""

#Using comments, create a header at the top of the program indicating the purpose of the program, assignment number, and your name
#Refer to the Submission Instructions for an example of an acceptable header
#done

#Use a print statement to print a welcome message for your user
welcome = ("Welcome to Fiber Supply - We Calculate and Install")
# print(welcome)

#Retrieve the company name from the user using input()
company_name = input("Enter Company Name: ")
# print (company_name)

#Retrieve the number of feet of fiber optic cable to be installed from the user using input()
feet_of_cable = float(input("Enter the Number of Feet of Cable: "))
# print (feet_of_cable)


#Calculate the installation cost of fiber optic cable by multiplying the number of feet requested by the user by $.95 per foot
cost_per_foot = 0.95
# print (cost_per_foot)
total_cost = round(feet_of_cable * cost_per_foot, 2)
# print (total_cost)

#Print a receipt for the user including the company name, number of feet of fiber to be installed, and total cost in a legible format
#Consider a receipt that you may receive when making a purchase
print(company_name, "Compay Receipt:")
print(f"Feet of Cable: {feet_of_cable:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

#Include appropriate comments throughout the program
#Your program should adhere to PEP8 guidelines including meaningful variable names
#Save your program with a meaningful filename such as lastname_week1.py
#done
#Must use good coding practices
