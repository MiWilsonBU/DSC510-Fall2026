# Purpose: Calculate the cost of a fiber optic cable installation and
#          provide the customer with a receipt.
# Assignment: Week 1 Programming Assignment
# Author: Yao Adoukonou


# Display a welcome message to the customer.
print("Welcome to the Fiber Optic Cable Installation Cost Calculator!")

# Collect the customer's company name and requested cable length.
company_name = input("Please enter your company name: ").strip()
fiber_length_feet = float(
    input("Enter the number of feet of fiber optic cable needed: ")
)

# Calculate the installation cost at $0.95 per foot.
cost_per_foot = 0.95
installation_cost = fiber_length_feet * cost_per_foot

# Display a clear, customer-friendly receipt.
print("\n" + "=" * 46)
print("       FIBER OPTIC INSTALLATION RECEIPT")
print("=" * 46)
print(f"Company:               {company_name}")
print(f"Fiber optic cable:     {fiber_length_feet:,.2f} feet")
print(f"Cost per foot:         ${cost_per_foot:,.2f}")
print("-" * 46)
print(f"Total installation:    ${installation_cost:,.2f}")
print("=" * 46)
print("Thank you for choosing our installation service!")
