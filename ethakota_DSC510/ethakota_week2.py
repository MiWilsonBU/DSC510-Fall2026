#!/usr/bin/env python3
# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Sandeep Ethakota
# 9/14/2026
#
# Purpose: Collects a company name and the number of feet of fiber
# optic cable requested by the user, calculates the total
# installation cost at $0.95 per foot, and prints a receipt
# for the user.
#
# Change Control Log:
# Change#: 1
# Change(s) Made: Added error handling to check for invalid cable-feet
#                  input (non-numeric values, commas, and "ft"/"feet"
#                  suffixes) in the get_cable_feet function
# Date of Change: 9/14/2026
# Author: Sandeep Ethakota
# Change Approved by: Sandeep Ethakota
# Date Moved to Production: 9/14/2026

import logging

# ---------------------------------------------------------------------
# Configure logging so that any unexpected errors are written to a
# log file instead of crashing the program with a raw traceback.
# ---------------------------------------------------------------------
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Cost per foot of fiber optic cable, in US dollars.
COST_PER_FOOT = 0.95


def get_company_name():
    """Prompt the user for their company name and return it.

    A simple validation loop makes sure the user does not submit an
    empty company name, since that would produce an unusable receipt.
    """
    while True:
        company_name = input("Please enter your company name: ").strip()
        if company_name:
            return company_name
        print("Company name cannot be blank. Please try again.\n")


def get_cable_feet():
    """Prompt the user for the number of feet of cable requested.

    Uses a try/except block to catch non-numeric input. Common,
    non-developer-friendly formatting (thousands separators like
    "1,200" or a trailing unit like "250 ft") is cleaned up before
    conversion so everyday users are not penalized for typing
    numbers the way they naturally would. Invalid entries are logged
    to error_log.txt and the user is asked again instead of the
    program crashing.
    """
    while True:
        feet_input = input(
            "Please enter the number of feet of fiber optic cable "
            "to be installed: "
        )

        # Clean up common, non-developer-friendly formatting before
        # attempting to convert the value to a number.
        cleaned_input = feet_input.strip().lower()
        cleaned_input = cleaned_input.replace(",", "")
        cleaned_input = cleaned_input.replace("ft", "")
        cleaned_input = cleaned_input.replace("feet", "")
        cleaned_input = cleaned_input.strip()

        try:
            cable_feet = float(cleaned_input)
            if cable_feet < 0:
                raise ValueError("Feet of cable cannot be negative.")
            return cable_feet
        except ValueError as error:
            logging.error(
                "Invalid cable feet input '%s': %s", feet_input, error
            )
            print(
                "That doesn't look like a valid, non-negative number. "
                "Please enter numbers only (example: 250 or 1,200).\n"
            )


def calculate_installation_cost(cable_feet):
    """Calculate the total installation cost.

    Cost is simply the number of feet requested multiplied by the
    fixed cost per foot.
    """
    total_cost = cable_feet * COST_PER_FOOT
    return total_cost


def print_receipt(company_name, cable_feet, total_cost):
    """Print a formatted, easy-to-read receipt for the user."""
    print("\n" + "=" * 40)
    print("       FIBER OPTIC INSTALLATION RECEIPT")
    print("=" * 40)
    print(f"Company Name:      {company_name}")
    print(f"Feet of Cable:     {cable_feet:,.2f} ft")
    print(f"Cost Per Foot:     ${COST_PER_FOOT:.2f}")
    print("-" * 40)
    print(f"Total Cost:        ${total_cost:,.2f}")
    print("=" * 40 + "\n")


def main():
    """Main program flow: welcome the user, gather input, and show the
    final receipt.
    """
    # Welcome message for the user.
    print("Welcome to the Fiber Optic Cable Installation Calculator!")
    print("Let's get some information to prepare your installation "
          "receipt.\n")

    # Gather required information from the user.
    company_name = get_company_name()
    cable_feet = get_cable_feet()

    # Perform the cost calculation.
    total_cost = calculate_installation_cost(cable_feet)

    # Display the final receipt to the user.
    print_receipt(company_name, cable_feet, total_cost)


if __name__ == "__main__":
    main()
