# Mitchell Brady
# DSC 510
# 2026-09-19
# Week 2: Calculate Item Cost and Print Receipt
# Description: This program will prompt the user for their company name
#              and how much fiber optic cable they wish to purchase. It
#              will then calculate their cost and print out a human-readable receipt
from typing import Final

# Fixed cost of Fiber Optic cable
FIBER_OPTIC_COST: Final[float] = 0.95

def main():
    company_name = input("Welcome: Please input your company name: ")
    fiber_optic_cable_quantity = int(input("Please input quantity of fiber optic cable by feet: "))

    # Calculate the total cost for our user
    total_cost = fiber_optic_cable_quantity * FIBER_OPTIC_COST

    # Print Receipt
    print("--------------------------------------------------")
    print(f"Receipt for {company_name}")
    print()
    print(f"{fiber_optic_cable_quantity}x Fiber Optic Cable (per foot): \t\t${total_cost}")
    print()
    print("Thank you for shopping with us!")
    print("--------------------------------------------------")

    return

if __name__ == '__main__':
    main()