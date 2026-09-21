# Purpose: Calculate the cost of a fiber optic cable installation using
#          quantity-based pricing and handle invalid numeric input.
# Assignment: Week 2 Programming Assignment
# Author: Yao Adoukonou


# Display a welcome message to the customer.
print(
    "Welcome to the Fiber Optic Cable Installation Cost Calculator!"
)

# Retrieve the customer's company name.
company_name = input("Please enter your company name: ").strip()

# Continue prompting until the customer enters a valid cable length.
while True:
    try:
        fiber_length_feet = float(
            input("Enter the number of feet of fiber optic cable needed: ")
        )

        # A cable length must be greater than zero.
        if fiber_length_feet <= 0:
            print("Please enter a number greater than zero.")
            continue

        break
    except ValueError:
        print("Invalid entry. Please enter the cable length as a number.")

# Determine the price per foot based on the requested cable length.
if fiber_length_feet > 500:
    cost_per_foot = 0.55
elif fiber_length_feet > 250:
    cost_per_foot = 0.75
elif fiber_length_feet > 100:
    cost_per_foot = 0.85
else:
    cost_per_foot = 0.95

# Calculate the total installation cost.
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
