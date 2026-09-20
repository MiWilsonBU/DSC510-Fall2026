# -----------------------------
# DSC 510
# Week 2
# Programming Assignment Week 2
# Author: Kevin Bratetic
# Date: 19 September 2026
# Modified By:
# Description: Calculates fiber optic cable installation cost
# and prints a customer receipt.
# Sources: No third-party code was reused.
# -----------------------------
# Change#: 1
# Change(s) Made: Initial program created
# Date of Change: 19 September 2026
# Author: Kevin Bratetic
# Change Approved by: Kevin Bratetic
# Date Moved to Production: 19 September 2026
# -----------------------------

# Price per foot from the assignment notes
COST_PER_FOOT = 0.95

# Welcome the user
print("Welcome to the Bratetic Fiber Optic Installation Cost Calculator")
print("This program estimates installation cost at $0.95 per foot.\n")

# Get the company name from the user
company_name = input("Enter your company name: ")

# Get the number of cable feet and convert it to a number
cable_feet = float(input("Enter the number of feet of fiber optic cable: "))

# Calculate the total installation cost
total_cost = cable_feet * COST_PER_FOOT

# Print a simple receipt
print("\n" + "=" * 40)
print("INSTALLATION RECEIPT")
print("=" * 40)
print(f"Company:           {company_name}")
print(f"Fiber requested:   {cable_feet} feet")
print(f"Price per foot:    ${COST_PER_FOOT:.2f}")
print("-" * 40)
print(f"Total cost:        ${total_cost:.2f}")
print("=" * 40)
print("We thank you for your business.")