# ============================================================================
# DSC 510: Introduction to Programming
# Week 2: Programming Assignment
# Program: Fiber Optic Cable Installation Cost Calculator
# Author: Rama Kammari
# Date: 9/20/2026
# Purpose: Calculate the installation cost of fiber optic cable for customers
#          by multiplying the requested footage by the cost per foot ($0.95)
#          and display a formatted receipt
# ============================================================================
# Change Control Log:
# Change#: 1
# Change(s) Made: Added error handling for invalid cable-feet input
#                  (letters, commas, "ft"/"feet") in get_feet()
# Date of Change: 9/20/2026
# Author: Rama Kammari
# Change Approved by: Rama Kammari
# Date Moved to Production: 9/20/2026

# Cost charged per foot of cable installed

# Define the cost per foot of fiber optic cable
COST_PER_FOOT = 0.95

# Display welcome message to the user
print("=" * 60)
print("Welcome to Fiber Optic Cable Installation Cost Calculator")
print("=" * 60)
print()

# Retrieve company name from user
company_name = input("Please enter the company name: ")

# Retrieve the number of feet of fiber optic cable from user
# Using a try-except block to ensure valid numeric input
while True:
    try:
        feet_of_cable = float(input("Enter the number of feet of fiber optic cable to install: "))
        # Validate that the input is positive
        if feet_of_cable < 0:
            print("Error: Please enter a positive number for footage.")
            continue
        break
    except ValueError:
        print("Error: Please enter a valid number.")

# Calculate the total installation cost
total_cost = feet_of_cable * COST_PER_FOOT

# Display a formatted receipt to the user
print()
print("=" * 60)
print("INSTALLATION RECEIPT")
print("=" * 60)
print()
print(f"Company Name:              {company_name}")
print(f"Feet of Fiber Optic Cable: {feet_of_cable:,.2f} feet")
print(f"Cost per Foot:             ${COST_PER_FOOT:.2f}")
print("-" * 60)
print(f"Total Installation Cost:   ${total_cost:,.2f}")
print()
print("=" * 60)
print("Thank you for your business!")
print("=" * 60)