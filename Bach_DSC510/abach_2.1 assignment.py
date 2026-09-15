"""
DSC 510 - Week 2 - 2.1 Assignment
Author: Andrew Bach
Date: 9/14/2026

Program used to calculate the cost of an order of fiber optic cable

Change Log:
    Change: 1
    Changes made: Moved logic into methods to improve readability
    Date of change: 9/14/2026
    Author: Andrew Bach
    Change Approved by: Andrew Bach
"""
import locale
locale.setlocale(locale.LC_ALL, 'C')

# Cost per foot of fiber optic cable
COST_PER_FOOT = 0.95


def format_currency(amount):
    return '${:,.2f}'.format(amount)


def get_company():
    company_name = ""

    while not company_name:
        company_name = input("\nWhat company are you ordering for: ").strip()

        if not company_name:
            print("Please enter a company name.")

    return company_name


def get_order_quantity():
    quantity = 0

    while quantity <= 0:
        try:
            quantity = int(input("\nHow many feet of fiber optic cable would you like to order: "))

            if quantity <= 0:
                print("Please enter a number greater than 0 for your order.")
                continue

            total = quantity * COST_PER_FOOT

            print(f"\n{quantity} feet of fiber optic cable will cost a total of {format_currency(total)}.")
            user_input = input("Would you like to proceed? (Y/N): ").upper()

            if user_input in ("N", "NO", "NOPE"):
                continue

        except ValueError:
            print("An invalid value was entered, please enter a numeric value for your order.")

    return quantity, total


def main():
    continue_ordering = True
    while continue_ordering:
        print("Welcome to the Bach Fiber Optics. Lets get ready to place your order!")

        company = get_company()

        print(
            f"\nWe are looking forward to helping {company} with their Fiber Optic Cable Order."
            "\n-Current Costs-"
            "\nFiber Optic Cable | $0.95 per foot"
        )

        order_quantity, order_total = get_order_quantity()

        # Print Receipt
        print(
            "\nYour order has been placed!"
            "\nHere is your receipt:"
            "\n-------------------------------------------"
            "\nBach Fiber Optics"
            "\n-------------------------------------------"
            f"\nSales Receipt for {company}"
            "\n-------------------------------------------"
            "\nQty     | Product                | Price"
            f"\n{order_quantity}      | Fiber optic cable      | {format_currency(order_total)}\n"
            f"\nTotal: {format_currency(order_total)}"
            "\n-------------------------------------------"
        )

        user_input = input("\nWould you like to place another order? (Y/N): ").upper()

        if user_input in ("N", "NO", "NOPE"):
            continue_ordering = False

if __name__ == "__main__":
    main()