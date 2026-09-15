# ------------------------------------------------------------------
# Program:     Fiber Optic Cable Installation Cost Calculator
# Assignment:  Week 1
# Author:      Candace Lucas
# Purpose:     Collects a company name and the number of feet of
#              fiber optic cable needed, calculates the installation
#              cost, and prints a receipt for the user.
# ------------------------------------------------------------------

# Price charged per foot of installed fiber optic cable
PRICE_PER_FOOT = 0.95

# Greet the user so they understand what this program does
print("Welcome to the Fiber Optic Cable Installation Cost Calculator!")
print()  # blank line for readability

# Collect the company name from the user
company_name = input("Please enter your company name: ")

# Collect the number of feet needed; convert text input to a number
feet_requested = float(input("Please enter the number of feet of fiber optic cable needed: "))

# Calculate the total installation cost
total_cost = feet_requested * PRICE_PER_FOOT

# Print a formatted receipt for the user
print()
print("----------------------------------------")
print("           INSTALLATION RECEIPT          ")
print("----------------------------------------")
print(f"Company Name:      {company_name}")
print(f"Feet Installed:    {feet_requested}")
print(f"Price per Foot:    ${PRICE_PER_FOOT:.2f}")
print(f"Total Cost:        ${total_cost:.2f}")
print("----------------------------------------")
print("Thank you for your business!")