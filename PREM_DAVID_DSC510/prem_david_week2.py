# DSC 510 PROGRAMMING
# Week 2
# Programming Assignment Week 2
# Author: Prem David
# Date: 9/19/2026

"""
Change Control Log:
Change #: 1
Change(s) Made: Initial creation of the fiber optic installation program
Date of Change: 9/19/2026
Author: Prem David
Change Approved by: N/A
Date Moved to Production: 9/19/2026
"""

"""
Purpose:
This program calculates the cost of installing fiber optic cable.
The user enters a company name and the number of feet of fiber optic
cable needed. The installation cost is calculated at $0.95 per foot,
and a formatted receipt is displayed.
"""

cost_per_foot = 0.95

# Method to get user input
def get_user_input():
    """Retrieve the company name and number of fiber optic feet."""
    company_name = input("Please enter the company name: ")
    fiber_feet = float(
        input("Please enter the number of feet of fiber optic cable needed: ")
    )
    return company_name, fiber_feet

# Method to calculate cost
def calculate_cost(fiber_feet):
    """Calculate the total fiber optic installation cost."""
    total_cost = fiber_feet * cost_per_foot
    return total_cost

# Main method
def main():
    """Run the fiber optic installation cost calculation."""

    # Display a welcome message to the user.
    print("Welcome to the Fiber Optic Installation Cost Calculation!")

    # Retrieve input from the user.
    company_name, fiber_feet = get_user_input()

    # Calculate the total installation cost.
    total_cost = calculate_cost(fiber_feet)

    # Display the receipt.
    print("\n=========================================")
    print("       FIBER OPTIC INSTALLATION")
    print("========================================")
    print(f"Company Name :       {company_name}")
    print(f"Length of Fiber Optic Cable :  {fiber_feet:,.2f} feet")
    print(f"Cost Per Foot :      ${cost_per_foot:.2f}")
    print("========================================")
    print(f"Total Cost:         ${total_cost:,.2f}")
    print("========================================")
    print("Thank you for your business!")


if __name__ == "__main__":
    main()