# Title: Assignment 2.1 Programming Assignment
# Author: Lois Yeung
# Date: 19 September 2026
# Modified By: Lois Yeung
# Description: This program accepts user input and calculates
# the installation cost for fiber optic cable.
#
# Change Control Log:
# Change #: 1
# Change(s) Made: Added validation loops for blank company-name entries,
# invalid cable-length entries, and cable lengths less than or equal to zero.
# Lines Added/Modified: 51-75
# Date of Change: 09/19/2026
# Author: Lois Yeung
# Change Approved By: N/A
# Date Moved to Production: N/A
#
# Change #: 2
# Change(s) Made: Moved receipt printing logic to its own function.
# Lines Added/Modified: 27-45
# Date of Change: 09/19/2026
# Author: Lois Yeung
# Change Approved By: N/A
# Date Moved to Production: N/A


def print_receipt(company_name, length_cable):
    PRICE_PER_FOOT = 0.95
    installation_cost = length_cable * PRICE_PER_FOOT

    print("\n" + "=" * 45)
    print("Epic Fiber Optic, LLC.".center(45))
    print("INSTALLATION RECEIPT".center(45))
    print("=" * 45)

    print(f"{'Company Name:':<22}{company_name}")
    print(f"{'Cable Length:':<22}{length_cable:,.2f} feet")
    print(f"{'Price per Foot:':<22}${PRICE_PER_FOOT:.2f}")

    print("-" * 45)
    print(f"{'TOTAL INSTALLATION COST:':<28}"
          f"${installation_cost:>14,.2f}")
    print("=" * 45)

    print("\nThank you for using Epic Fiber Optic!")


print("Welcome to Epic Fiber Optic!")

# Keep asking until the company name is not empty.
while True:
    # Remove leading/trailing spaces so spaces-only input is treated as blank.
    company_name = input("What is the name of your company? ").strip()

    if company_name:
        break

    print("Company name cannot be blank. Please try again.")

# Keep asking until the cable length is numeric and greater than zero.
while True:
    try:
        cable_prompt = "What is the length of your cable (in feet)? "
        # Remove leading/trailing spaces so spaces-only input is treated as blank.
        length_cable = float(input(cable_prompt).strip())

        if length_cable > 0:
            break

        print("Cable length must be greater than zero. Please try again.")

    except ValueError:
        print("Please enter a valid numeric cable length.")

print_receipt(company_name, length_cable)