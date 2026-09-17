#DSC 510
#Week 2
#Programming Assignment Week 2
#Author: Abrham Worabo
#9/16/2024

# Fixed installation rate, in dollars per foot of fiber optic cable
COST_PER_FOOT = 0.95

# Greet the user
print("Welcome to the Fiber Optic Cable Installation Cost Calculator!")
print()

#Collect the company name from the user
company_name = input("Please enter your company name: ")

#Collect the number of feet of cable to install, converting to a float
#so partial-foot amounts are supported
feet_requested = float(input("Please enter the number of feet of fiber optic cable to install: "))

# Calculate the total installation cost
total_cost = feet_requested * COST_PER_FOOT

# formatted receipt for the user
print()
print("=" * 45)
print("           INSTALLATION RECEIPT ")
print("=" * 45)
print(f"Company:            {company_name}")
print(f"Feet of Cable:      {feet_requested:.2f} ft")
print(f"Rate per Foot:      ${COST_PER_FOOT:.2f}")
print("-" * 45)
print(f"Total Cost:         ${total_cost:,.2f}")
print("=" * 45)
print("Thank you for your business!")
