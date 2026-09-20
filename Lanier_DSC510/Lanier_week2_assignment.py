#----------------------------------------------------------------------------------------------------------
# DSC 510
# Week 2
# Week 2 assignement: Goal is to build a user input script to generate the total cos tof fiber optic cable
# Author: Jack Lanier
# 09/20/2026
# ---------------------------------------------------------------------------------------------------------

# print the welcome message
print("Welcome to the Fiber Optic Cable Calculator")

# Get the company name from user input
company_name = input("Please input the company name: ")

# Get the number of feet of fiber optic cable
feet_requested = float(input("Please input the feet requested: "))

# The cost per foot
cost_per_foot = 0.95

# Calculate the total instalation cost
total_cost = cost_per_foot * feet_requested

#Print as a reciept

print("\n ------------------RECEIPT------------------")
print(f"Company Name: {company_name}")
print(f"Feet of Cable to Install: {feet_requested:.2f} ft")
print(f"Total Cost: ${total_cost:.2f}")
print("--------------------------------------------")