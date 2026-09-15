#!/usr/bin/env python3
# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Sandeep Ethakota
# 9/14/2026
#
# Purpose: Ask the user for a company name and the number of feet of
# fiber optic cable they need installed, calculate the total cost at
# $0.95 per foot, and print out a receipt.
#
# Change Control Log:
# Change#: 1
# Change(s) Made: Added error handling for invalid cable-feet input
#                  (letters, commas, "ft"/"feet") in get_feet()
# Date of Change: 9/14/2026
# Author: Sandeep Ethakota
# Change Approved by: Sandeep Ethakota
# Date Moved to Production: 9/14/2026

# Cost charged per foot of cable installed
COST_PER_FOOT = 0.95


def get_company_name():
    # ask the user for their company name, don't allow it to be blank
    name = input("Please enter your company name: ")
    while name.strip() == "":
        print("Company name can't be blank, try again.")
        name = input("Please enter your company name: ")
    return name


def get_feet():
    # ask the user how many feet of cable they need, keep asking
    # until we get a real number back
    while True:
        feet_input = input(
            "Please enter the number of feet of fiber optic cable "
            "to be installed: "
        )

        # people might type things like "1,200" or "250 ft" instead
        # of just a plain number, so clean that up first
        cleaned = feet_input.strip().lower()
        cleaned = cleaned.replace(",", "")
        cleaned = cleaned.replace("feet", "")
        cleaned = cleaned.replace("ft", "")
        cleaned = cleaned.strip()

        try:
            feet = float(cleaned)
            if feet < 0:
                print("Feet can't be negative, please try again.\n")
                continue
            return feet
        except ValueError:
            # write the bad input to a log file so we have a record
            # of it, then let the user try again instead of crashing
            log_file = open("error_log.txt", "a")
            log_file.write("Invalid feet entered: " + feet_input + "\n")
            log_file.close()
            print("That's not a valid number. Please enter numbers "
                  "only (example: 250 or 1,200).\n")


def main():
    print("Welcome to the Fiber Optic Cable Installation Calculator!")
    print("Let's get some information for your receipt.\n")

    company_name = get_company_name()
    feet = get_feet()

    # do the math - total cost is feet times cost per foot
    total_cost = feet * COST_PER_FOOT

    # print out the receipt
    print("\n========================================")
    print("     FIBER OPTIC INSTALLATION RECEIPT")
    print("========================================")
    print("Company Name:   ", company_name)
    print("Feet of Cable:  ", feet, "ft")
    print("Cost Per Foot:   $" + str(COST_PER_FOOT))
    print("----------------------------------------")
    print("Total Cost:      $" + str(round(total_cost, 2)))
    print("========================================\n")


main()
